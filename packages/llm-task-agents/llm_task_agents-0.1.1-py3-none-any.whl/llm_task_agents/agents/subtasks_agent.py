from ollama import Client
import json
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class SubTasksAgent:
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
		# if no user request, return None
		if not user_request.strip():
			return None

		# Get database schema and build prompts
		database_schema = self.get_database_schema_bullet(tables)

		# build prompt
		prompts = self.build_prompts(user_request, database_schema)

		# query LLM
		retry = 0
		while retry < max_retry:
			try:
				response = self.llm.generate(
					model=self.model,
					system=prompts["system_prompt"],
					prompt=prompts["prompt"],
					format="json"
				)

				if self.debug:
					print(response)

				if "response" in response:
					# validate and return JSON
					generated_json = json.loads(response["response"])

					if self.debug:
						print(generated_json)

					return generated_json
			except Exception as e:
				if self.debug:
					print(f"Error: {e}, retrying...")
				else:
					pass

			retry += 1

		return None

	def remove_leading_based_on_second_line(self, text: str) -> str:
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
		# Enhanced system prompt that decides if subtasks are necessary
		system_prompt = """
		You are an intelligent agent that elaborates a plan to fulfill the user's request. Your job is to:
		- Break the request into multiple, smaller tasks descriptions, not SQL queries, each focusing on specific data retrieval.
		- Each task description must be completely independent, including any necessary information such as fields, filters, constraints, and any relevant relationships between tables. Do not refer to the results of other tasks for context or information.
		- Use consistent constraints or filters across all tasks, ensuring that no task depends on another.
		- Use IDs only in JOIN conditions but exclude them from the SELECT clause. Ensure that the query returns only relevant textual or meaningful data, not IDs.
		- If a single, complex task can fulfill the request effectively, return that task instead of breaking it down.
		- If you expect data that could be nicely represented in a plotly graph, set "true" for the "graph" field, otherwise set "false."
		- Return the task descriptions in an ordered JSON list format, where each task stands alone, or a single task when relevant.
		- Return only the JSON list using the following structure:
		{{
			'tasks': 
				[
					{{
						'task': '<task description>',
						'type': 'table',
						'title': '<task title>',
						'graph': '<boolean_value>'
					}},
				]
		}}
		"""

		prompt_template = """
		Database Schema:
		{database_schema}

		User's Request:
		{user_request}
		"""

		# Format the prompt with the actual database schema and user request
		prompt = prompt_template.format(
			database_schema=str(database_schema).strip(),
			user_request=str(user_request).strip()
		)

		# Clean up prompts by removing leading whitespace
		system_prompt = self.remove_leading_based_on_second_line(system_prompt)
		prompt = self.remove_leading_based_on_second_line(prompt)

		if self.debug:
			print(system_prompt)
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
	
	def list_tables(self):
		return [table_name for table_name in self.metadata.tables.keys()]