import os
import unittest
import pandas as pd
from llm_task_agents.agent_factory import GraphAgent

class TestGraphAgent(unittest.TestCase):

	def setUp(self):
		"""Set up the environment and GraphAgent for testing"""
		self.llm_api_url = os.getenv("OLLAMA_API_BASE")
		self.graph_agent = GraphAgent(
			llm_api_url=self.llm_api_url, 
			model="llama3.2:3b",
			debug=False
		)
		self.user_request = "Generate a bar chart for sales data by region."
		
		# Create a sample DataFrame
		self.df = pd.DataFrame({
			"region": ["North", "South", "East", "West"],
			"sales": [100, 150, 200, 120]
		})

	def test_graph_agent(self):
		"""Test that the GraphAgent returns a valid base64-encoded image and graph title"""
		html, svg, img_base64, graph_title = self.graph_agent.run(
			user_request=self.user_request, 
			df=self.df
		)

		# Test that a valid base64 image string is returned
		self.assertIsNotNone(img_base64, "GraphAgent should return a base64 encoded image")
		self.assertTrue(isinstance(img_base64, str) and len(img_base64) > 0, "Image string should be valid")

		# Test that a valid graph title is returned
		self.assertIsNotNone(graph_title, "GraphAgent should return a graph title")
		self.assertTrue(isinstance(graph_title, str) and len(graph_title) > 0, "Graph title should be a valid string")

if __name__ == "__main__":
	unittest.main()
