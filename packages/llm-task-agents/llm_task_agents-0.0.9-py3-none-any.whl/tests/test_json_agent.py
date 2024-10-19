import os
import unittest
from llm_task_agents.agent_factory import AgentFactory  # Absolute import based on package structure

class TestJSONAgent(unittest.TestCase):

    def setUp(self):
        """Set up the environment and agent for testing"""
        self.llm_api_url = os.getenv("OLLAMA_API_BASE")
        self.json_agent = AgentFactory.get_agent(
            agent_type="json", 
            llm_api_url=self.llm_api_url, 
            model="llama3.2:3b"
        )
        self.task = "Create 3 detailed, realistic character personas for a fantasy adventure game."
        
        # Define one item JSON structure
        person = {
            "first_name": "string", 
            "last_name": "string", 
            "age": "int", 
            "gender": "string", 
            "job": "string", 
            "description": "string"
        }

        # Define structure for a list of items
        self.structure = {
            "personas": [person for _ in range(3)]
        }

    def test_json_structure(self):
        """Test JSON structure returned by the agent"""
        result = self.json_agent.run(
            task=self.task, 
            structure=self.structure
        )

        # Check if 'personas' exists in the returned result
        self.assertIn("personas", result, "The result should contain the 'personas' key")

        # Check that the returned structure has the expected number of personas
        self.assertEqual(len(result["personas"]), 3, "The result should contain 3 personas")

        # Check that each persona has the expected fields
        for persona in result["personas"]:
            self.assertIn("first_name", persona)
            self.assertIn("last_name", persona)
            self.assertIn("age", persona)
            self.assertIn("gender", persona)
            self.assertIn("job", persona)
            self.assertIn("description", persona)

if __name__ == "__main__":
    unittest.main()
