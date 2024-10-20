import os
import unittest
from llm_task_agents.agent_factory import AgentFactory

class TestImageClassificationAgent(unittest.TestCase):

	def setUp(self):
		"""Set up the environment and agent for testing"""
		self.llm_api_url = os.getenv("OLLAMA_API_BASE")
		self.image_agent = AgentFactory.get_agent(
			agent_type="image", 
			llm_api_url=self.llm_api_url, 
			model="minicpm-v:8b-2.6-fp16",
		)
		self.image_path = "tests/images/watermelon.jpg"
		self.labels = [
			"Apple", "Lemon", "Cherry", "Orange", "Banana", 
			"Pineapple", "Melon", "Watermelon", "Peach", "Grape"
		]

	def test_image_classification(self):
		"""Test image classification functionality"""
		label = self.image_agent.run(
			image_path=self.image_path, 
			labels=self.labels
		)
		self.assertIn(label, self.labels, f"Returned label '{label}' is not in the expected labels")

if __name__ == "__main__":
	unittest.main()
