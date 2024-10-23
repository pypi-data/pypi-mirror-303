import os
import ollama

class ImageClassificationAgent:
	def __init__(self, llm_api_url:str, model:str, debug:bool=False):
		self.debug = debug
		self.llm_api_url = llm_api_url
		self.model = model
		self.llm = ollama.Client(host=llm_api_url)

	def run(self, image_path, labels, max_retry=3):
		if not os.path.isfile(image_path):
			print(f"Image path {image_path} does not exist")
			return None
		
		prompts = self.build_prompts(labels)

		if self.debug:
			print(f"Prompts:\n{prompts}")

		label = None
		retry = 0
		while retry < max_retry:
			retry += 1
			response = self.llm.chat(
				model=self.model,
				messages=[
					{
						'role': 'system',
						'content': prompts["system_prompt"],
					},
					{
						'role': 'user',
						'content': prompts["prompt"],
						'images': [image_path],
					}
				]
			)

			if self.debug:
				print(response)

			if response["message"]["content"] in labels:
				label = response["message"]["content"]
				break

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
	
	def format_labels(self, labels):
		formatted_labels = "Possible labels:\n" + "\n".join(labels)
		return formatted_labels
	
	def build_prompts(self, labels: list)-> dict:
		labels_string = self.format_labels(labels)

		system_prompt = """
		You are an assistant tasked with classifying images. Follow these guidelines:
		- You will be provided with an image and a list of possible labels.
		- Carefully analyze the image and select the single most appropriate label from the list.
		- Return only the label, without any explanation or additional text.
		"""

		prompt_template = """
		Possible labels:
		{labels}
		"""

		prompt = prompt_template.format(
			labels=str(labels_string).strip(),
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

