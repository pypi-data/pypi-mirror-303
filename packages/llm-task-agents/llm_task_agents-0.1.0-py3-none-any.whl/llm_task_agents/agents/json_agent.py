from ollama import Client
import json

class JSONAgent:
	def __init__(self, llm_api_url:str, model:str, debug:bool=False)->None:
		self.debug = debug

		self.llm_api_url = llm_api_url
		self.model = model

		self.llm = Client(host=llm_api_url)

	def run(self, task:str, structure: dict, max_retry:int=3)->list:
		# if no tasks, return empty list
		if not task.strip():
			return None

		# build prompt
		prompts = self.build_prompts(task, structure)

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
					# validate JSON
					generated_json = json.loads(response["response"])
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

	def build_prompts(self, task: str, structure: dict) -> str:
		system_prompt = """
		You are an assistant tasked with generating valid JSON. Follow these guidelines:
		- The output should be a JSON object or array.
		- Ensure the JSON is correctly structured with proper use of keys and values.
		- Do not include any extra explanations, just the JSON output.
		"""

		prompt_template = """
		Answer the user's query:
		{task}

		With the following JSON structure:
		{structure}
		"""

		prompt = prompt_template.format(
			task=str(task),
			structure=json.dumps(structure, indent=4),
		)

		# clean up prompts
		system_prompt = self.remove_leading_based_on_second_line(system_prompt)
		prompt = self.remove_leading_based_on_second_line(prompt)

		if self.debug:
			print(system_prompt)
			print(prompt)

		return {
			"system_prompt": system_prompt,
			"prompt": prompt
		}

