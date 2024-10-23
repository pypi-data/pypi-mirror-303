import ollama

class TextClassificationAgent:
	def __init__(self, llm_api_url:str, model:str, debug:bool=False):
		self.debug = debug
		self.llm_api_url = llm_api_url
		self.model = model
		self.llm = ollama.Client(host=llm_api_url)

	def run(self, text: str, labels: list, max_retry: int = 3) -> str:
		if not text.strip():
			return None

		# Generate prompts based on the text and labels
		prompts = self.build_prompts(text, labels)

		# Debugging: Print prompts if debugging is enabled
		if self.debug:
			print(f"Prompts:\n{prompts}")

		label = None
		retry = 0

		while retry < max_retry:
			retry += 1

			# Generate response from the LLM
			try:
				response = self.llm.generate(
					model=self.model,
					system=prompts["system_prompt"],
					prompt=prompts["prompt"],
				)
			except Exception as e:
				if self.debug:
					print(f"Error during LLM call: {e}")
				continue  # Retry if there's an error

			# Debugging: Print the response if debugging is enabled
			if self.debug:
				print(f"Response from LLM: {response.get('response', 'No response')}")

			# Safely extract and clean the response
			response_key = str(response.get("response", "")).replace('"', "").replace("'", "").strip().lower()

			# Compare cleaned response with lowercase labels (convert list to lowercase)
			labels_lower = [label.lower() for label in labels]
			
			if response_key in labels_lower:
				# Find the original label from the list using its index (case-insensitive match)
				label = labels[labels_lower.index(response_key)]
				break  # Exit loop when the correct label is found

		return label
	
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
	
	def build_prompts(self, text:str, labels:list)-> dict:
		system_prompt = """
		You are an assistant tasked with classifying text. Follow these guidelines:
		- You will be provided with a text and a list of possible labels.
		- Carefully analyze the text and select the single most appropriate label from the list.
		- Return only one label from the list, without any explanation or additional text.
		"""

		prompt_template = """
		Text:
		{text}

		Possible labels:
		{labels}
		"""

		prompt = prompt_template.format(
			text=str(text).strip(),
			labels=str("\n".join(labels)).strip(),
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

