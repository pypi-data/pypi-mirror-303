from ollama import Client
import re
import pandas as pd
import io
import darkdetect
import json
import base64
import plotly.express as px

class GraphAgent:
	def __init__(
		self,
		llm_api_url: str,
		model: str,
		debug: bool = False,
	):
		self.debug = debug

		# LLM configurations
		self.llm_api_url = llm_api_url
		self.model = model

		self.llm = Client(host=llm_api_url)

	def run(self, user_request: str, df: pd.DataFrame, max_retry: int = 3) -> str:
		# Get database schema and build initial prompts
		prompts = self.build_prompts(user_request=user_request, df=df)
		original_prompt = prompts["prompt"]

		# Initialize error list
		errors = []

		# Retry loop for generating the correct code
		for retry in range(max_retry):
			try:
				# Query LLM
				response = self.llm.generate(
					model=self.model,
					system=prompts["system_prompt"],
					prompt=prompts["prompt"],
					format="json",
					stream=False,
				)

				if self.debug:
					print("Response:")
					try:
						print(response["response"])
					except:
						print(response)

				if "response" in response:
					# Extract code and graph title from the LLM response
					code = "\n".join(
						self.extract_code_blocks(
							llm_response=response["response"],
							expected_json_keys=["code"]
						)
					)

					graph_title = " ".join(
						self.extract_code_blocks(
							llm_response=response["response"],
							expected_json_keys=["graph_title"]
						)
					).strip()

					# Execute the generated code with error handling
					try:
						# Create a local dictionary with necessary imports and variables
						local_vars = {'df': df, 'pd': pd, 'px': px}
						exec(code, {}, local_vars)
						fig = local_vars.get('fig')

						if fig:
							# Force background color based on system theme
							background_color = '#181A1B' if darkdetect.isDark() else 'white'
							fig.update_layout(
								plot_bgcolor=background_color,
								paper_bgcolor=background_color,
								width=1024,
								height=400
							)
							
							# Convert figure to image bytes and encode as base64
							img_bytes = fig.to_image(format="png")
							img_base64 = base64.b64encode(img_bytes).decode('ascii')
							
							return img_base64, graph_title
						else:
							print("No fig created in generated code.")
							return None, graph_title  # Explicitly return None if fig is not created

					except Exception as e:
						# Append each failed attempt and error to the prompt for the next LLM query
						error_message = f"Previous attempt {retry + 1}:\n{code}\n\nExecution error:\n{str(e)}"
						errors.append(error_message)

						print(f"Error executing generated code: {e}")

						# Update the prompt with each appended error for the next retry
						prompts["prompt"] = f"{original_prompt}\n\n" + "\n\n".join(errors)

			except Exception as e:
				print(f"Error querying LLM: {e}. Retrying with the same prompt.")
				# Do not change the prompt, just retry

		return None, None  # Return None if max retries exceeded

	def extract_code_blocks(self, llm_response, expected_json_keys=None):
		code_blocks = []

		# Define the unwanted keywords
		unwanted_keywords = [
			'import', '```', 'IPython', 'IFrame', 'DisplayHTML', 'plt.show()', 
			'fig.show()', 'savefig', 'write_html', 'write_image', '.save', '.show'
		]

		def validate_and_extract_json(json_block):
			"""
			Validate that the JSON block contains the expected keys (case-insensitive).
			Return only the values for the expected keys.
			"""
			try:
				parsed_json = json.loads(json_block)
				if expected_json_keys:
					# Create a lowercase mapping of the JSON keys
					lower_keys_json = {k.lower(): v for k, v in parsed_json.items()}
					# Extract and return the values for the expected keys (case-insensitive)
					extracted_values = [
						lower_keys_json.get(key.lower())
						for key in expected_json_keys
						if key.lower() in lower_keys_json
					]
					# If all expected keys are found, return the extracted values
					if len(extracted_values) == len(expected_json_keys):
						return extracted_values
					else:
						return None
				else:
					return None
			except json.JSONDecodeError:
				return None

		# Function to filter unwanted keywords from code
		def filter_unwanted_keywords(code):
			return "\n".join([line for line in code.splitlines() if not any(keyword in line for keyword in unwanted_keywords)])

		# First, try to extract JSON directly from the raw input if it's not wrapped in a code block
		valid_json = validate_and_extract_json(llm_response)
		if valid_json:
			filtered_json = [filter_unwanted_keywords(value) for value in valid_json]
			code_blocks.extend(filtered_json)

		# Regex to match code blocks (with or without language hints)
		code_block_pattern = re.compile(r'```(?:[a-zA-Z]+\n)?(.*?)```', re.DOTALL)

		# Find all code blocks (even those with language hints)
		matches = code_block_pattern.findall(llm_response)

		# Process each code block
		for match in matches:
			match = match.strip()  # Strip any surrounding whitespace

			# Attempt to extract and validate JSON from the matched code block
			valid_json_in_block = validate_and_extract_json(match)

			# Add the valid JSON values (e.g., SQL query) to code_blocks if they match the expected keys
			if valid_json_in_block:
				filtered_json_in_block = [filter_unwanted_keywords(value) for value in valid_json_in_block]
				code_blocks.extend(filtered_json_in_block)  # Extend with the extracted and filtered values

		return code_blocks

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

	def build_prompts(self, user_request: str, df: pd.DataFrame) -> dict:
		system_prompt = """
		You are an assistant tasked with generating Python code for Plotly figures. Follow these guidelines:
		- You will be provided with a pandas DataFrame and required plot details.
		- Generate valid Python code that creates a Plotly figure object based on the data.
		- The figure object must be assigned to a variable named 'fig'.
		- Choose the best Plotly graph type and set an appropriate title for the figure.
		- Do not include any import statements, display, or save functions.
		- Only provide code to create the figure and assign it to 'fig'.
		"""

		prompt_template = """
		Generated code will be executed with:
		```python
		local_vars = {{'df': df, 'pd': pd, 'px': px}}
		exec(code, {{}}, local_vars)
		```

		User request: {user_request}

		DataFrame info:
		{dataframe_info}

		DataFrame describe:
		{dataframe_describe}

		DataFrame shape:
		{dataframe_shape}

		DataFrame types:
		{dataframe_types}

		DataFrame head:
		{dataframe_head}

		Only answer with the following JSON structure:
		{{
			"graph_title": "<appropriate graph title>",
			"code": "<Python code that creates a Plotly figure named fig>",
		}}
		"""

		# Capture DataFrame info as a string
		buffer = io.StringIO()
		df.info(buf=buffer)
		dataframe_info = buffer.getvalue()

		prompt = prompt_template.format(
			theme="dark (graph background must be: #181A1B)" if darkdetect.isDark() else "light (graph background must be: white)",
			user_request=user_request,
			dataframe_info=dataframe_info.strip(),
			dataframe_describe=df.describe().to_string().strip(),
			dataframe_shape=df.shape,
			dataframe_types=df.dtypes.to_string().strip(),
			dataframe_head=df.head().to_string().strip()
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
	