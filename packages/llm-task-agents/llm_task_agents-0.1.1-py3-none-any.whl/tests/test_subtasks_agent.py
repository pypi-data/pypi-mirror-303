import os
import unittest
from unittest.mock import patch
from ollama import Client
from sqlalchemy import create_engine
from llm_task_agents.agent_factory import SubTasksAgent  # Replace with actual module path

class TestSubTasksAgent(unittest.TestCase):

    def setUp(self):
        """Set up the environment and agent for testing"""
        self.llm_api_url = os.getenv("OLLAMA_API_BASE", "http://localhost:8000")
        self.subtasks_agent = SubTasksAgent(
            llm_api_url=self.llm_api_url,
            model="llama3.2:3b",
            database_driver="mysql",
            database_username=os.getenv("MYSQL_USER", "default_user"),
            database_password=os.getenv("MYSQL_PASSWORD", "default_password"),
            database_host=os.getenv("MYSQL_HOST", "localhost"),
            database_port="3306",
            database_name="chinook",
            debug=True
        )
        self.user_request = "Sales per year"
        self.tables = ["customer", "invoice"]
        self.allowed_statements = ["SELECT"]

    @patch('builtins.input', side_effect=["test_user"])
    @patch('getpass.getpass', side_effect=["test_password"])
    def test_run_subtasks_agent(self, mock_input, mock_getpass):
        """Test SubTasksAgent query execution"""
        response = self.subtasks_agent.run(
            user_request=self.user_request,
            tables=self.tables,
            allowed_statements=self.allowed_statements
        )
        # Check that the response is not None and is a valid JSON-like structure
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 0, "The response should not be empty")
        self.assertIn('tasks', response, "Response should contain 'tasks' key")

if __name__ == "__main__":
    unittest.main()
