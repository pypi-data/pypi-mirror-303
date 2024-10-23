from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ollama import Client
import re

class SQLAgent:
	def __init__(
		self,
		llm_api_url: str,
		model: str,
		database_driver: str,
		database_username: str,
		database_password: str,
		database_host: str,
		database_port: str,
		database_name: str,
		debug: bool = False,
	):
		self.debug = debug

		# LLM configurations
		self.llm_api_url = llm_api_url
		self.model = model

		self.llm = Client(host=llm_api_url)

		# Database configuration
		self.database_driver = database_driver
		database_url = f"{self.database_driver}://{database_username}:{database_password}@{database_host}:{database_port}/{database_name}"
		self.engine = create_engine(database_url)
		Session = sessionmaker(bind=self.engine)
		self.session = Session()

		# Create metadata and reflect it from the database
		self.metadata = MetaData()
		self.metadata.reflect(bind=self.engine)

	def run(self, user_request: str, tables: list = None, allowed_statements: list = None, max_retry: int = 3) -> str:
		# Default allowed statements
		if allowed_statements is None:
			allowed_statements = ["SELECT"]

		# Get database schema and build prompts
		database_schema = self.get_database_schema_bullet(tables)
		# print(f"Tables:\n{tables}")
		# print(f"Database Schema:\n{database_schema}")
		prompts = self.build_prompts(user_request=user_request, database_schema=database_schema)
		original_prompt = prompts["prompt"]

		# Initialize errors array
		errors = []

		# Query LLM
		retry = 0
		while retry < max_retry:
			try:
				response = self.llm.generate(
					model=self.model,
					system=prompts["system_prompt"],
					prompt=prompts["prompt"],
				)

				if self.debug:
					print("Response:")
					try:
						print(response["response"])
					except:
						print(response)

				if "response" in response:
					sql_query = self.extract_sql_query(response["response"])

					# Check if query is allowed
					if sql_query.split()[0].upper() not in allowed_statements:
						if self.debug:
							print(f"Disallowed statement: {sql_query.split()[0]}")
						return None

					# Validate SQL syntax using EXPLAIN
					syntax_valid, error_message = self.validate_sql_syntax(sql_query)
					if syntax_valid:
						return sql_query
					else:
						if self.debug:
							print(f"Syntax error in generated SQL:\n{error_message}")
						# Append the error message and the problematic query to the errors array
						errors.append({
							"query": sql_query,
							"error": error_message
						})

						# Build a summary of errors to include in the prompt
						error_summary = "\n".join([
							f"Previous attempts #{idx + 1}: The query:\n'{err['query']}'\n\nhad the following error:\n{err['error']}\n"
							for idx, err in enumerate(errors)
						])

						# Modify the prompt to help LLM correct the query
						prompts["prompt"] = (
							f"{original_prompt}\n\n"
							f"{error_summary}\n\n"
							f"Please provide a corrected SQL query for the user's request:\n{user_request}"
						)

						if self.debug:
							print(f"Modified prompt:\n{prompts['prompt']}")

						# Retry the query
						retry += 1
						continue
			except Exception as e:
				if self.debug:
					print(f"Error: {e}, retrying...")
				else:
					raise e
			retry += 1
		return None  # Return None if max retries exceeded

	def validate_sql_syntax(self, sql_query: str) -> tuple[bool, str]:
		# Use EXPLAIN to check the syntax of the SQL query
		try:
			explain_query = f"EXPLAIN {sql_query}"
			with self.engine.connect() as connection:
				connection.execute(text(explain_query))
			return True, ""
		except Exception as e:
			error_message = str(e)
			
			# replace EXPLAIN
			error_message = error_message.replace("EXPLAIN ", "")
			
			# remove the last line
			error_message = error_message.rsplit('\n', 1)[0]

			return False, error_message

	def remove_leading_based_on_second_line(self, text: str) -> str:
		# Existing implementation
		# Split the text into lines
		lines = text.splitlines()

		if len(lines) < 2:
			return text.strip()  # If there's only one line, return the stripped version

		# Detect the leading spaces or tabs on the second line
		second_line = lines[1]
		leading_whitespace = ''
		for char in second_line:
			if char in (' ', '\t'):
				leading_whitespace += char
			else:
				break

		# Process each line starting from the second one
		stripped_lines = []
		for line in lines:
			if line.startswith(leading_whitespace):
				# Remove the detected leading whitespace from each line
				stripped_lines.append(line[len(leading_whitespace):])
			else:
				stripped_lines.append(line)

		# Join the lines back together and return the result
		return "\n".join(stripped_lines).strip()

	def build_prompts(self, user_request: str, database_schema: str) -> dict:
		system_prompt = """
		You are an assistant tasked with generating SQL queries. Follow these guidelines:
		- You will be provided with a database schema and required query details.
		- Generate a single valid SQL query based on the structure and requirements.
		- Use IDs only in JOIN conditions but exclude them from the SELECT clause. Ensure that the query returns only relevant textual or meaningful data, not IDs.
		- Sort the results in a way that aligns with the user's request intention. For example, if the request involves time, sort by date; if comparing values like revenue or sales, sort in descending order by the relevant metric.
		- Ensure correct syntax, table names, column names, and appropriate clauses (e.g., SELECT, WHERE, JOIN, ORDER BY).
		- Do not include explanations or comments in the output, only the SQL query.
		"""

		prompt_template = """
		{database_driver} database Schema:
		{database_schema}

		User's Request:
		{user_request}
		"""

		prompt = prompt_template.format(
			database_driver=str(self.database_driver).upper().strip(),
			database_schema=str(database_schema).strip(),
			user_request=str(user_request).strip(),
		)

		# Clean up prompts
		system_prompt = self.remove_leading_based_on_second_line(system_prompt)
		prompt = self.remove_leading_based_on_second_line(prompt)

		if self.debug:
			print("System Prompt:")
			print(system_prompt)
			print("\nUser Prompt:")
			print(prompt)

		return {
			"system_prompt": system_prompt,
			"prompt": prompt
		}

	def get_database_schema_bullet(self, tables: list = None) -> str:
		# print(f"Tables: {tables}")
		def get_column_details(column):
			col_type = str(column.type)
			if "COLLATE" in col_type:
				col_type = col_type.split("COLLATE")[0].strip()

			details = f"{column.name} ({col_type}"
			if column.primary_key:
				details += ", Primary Key"
			if column.foreign_keys:
				details += f", Foreign Key -> {' '.join([str(fk.target_fullname) for fk in column.foreign_keys])}"
			if column.nullable:
				details += ", Nullable"
			if column.default is not None:
				details += f", Default: {str(column.default.arg)}"
			details += ")"

			return details

		def format_as_bullet_points(table_name, columns):
			formatted_columns = "\n- ".join([get_column_details(col) for col in columns])
			return f"Table: {table_name}\n- {formatted_columns}\n"

		if tables is None:
			schema_bullet_points = [format_as_bullet_points(table_name, table.columns) for table_name, table in self.metadata.tables.items()]
		else:
			schema_bullet_points = [format_as_bullet_points(table_name, self.metadata.tables[table_name].columns) for table_name in tables if table_name in self.metadata.tables]

		return "\n".join(schema_bullet_points)

	def extract_sql_query(self, llm_response: str) -> str:
		# Remove code fences like ```sql or ```
		cleaned_response = re.sub(r'```(?:sql)?', '', llm_response, flags=re.IGNORECASE)
		cleaned_response = cleaned_response.strip('`')  # Remove any stray backticks at start/end

		# Strip leading/trailing whitespace from the entire response
		cleaned_response = cleaned_response.strip()

		# Split into lines to handle them individually
		lines = cleaned_response.splitlines()

		# Remove trailing whitespace from each line (optional)
		cleaned_lines = [line.rstrip() for line in lines]

		# Rejoin the lines to reconstruct the query
		cleaned_response = '\n'.join(cleaned_lines)

		if self.debug:
			print(f"Extracted SQL Query:\n{cleaned_response}")

		return cleaned_response

	def list_tables(self):
		return [table_name for table_name in self.metadata.tables.keys()]
