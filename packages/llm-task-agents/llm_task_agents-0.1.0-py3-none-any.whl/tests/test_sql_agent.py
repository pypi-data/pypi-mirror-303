import os
import unittest
from unittest.mock import patch
from llm_task_agents.agent_factory import AgentFactory  # Absolute import based on package structure

class TestSQLAgent(unittest.TestCase):

    def setUp(self):
        """Set up the environment and agent for testing"""
        self.llm_api_url = os.getenv("OLLAMA_API_BASE")
        self.sql_agent = AgentFactory.get_agent(
            agent_type="sql", 
            llm_api_url=self.llm_api_url, 
            model="llama3.2:3b", 
            database_driver="mysql", 
            database_username=os.getenv("MYSQL_USER", "default_user"), 
            database_password=os.getenv("MYSQL_PASSWORD", "default_password"),
            database_host=os.getenv("MYSQL_HOST", "localhost"), 
            database_port="3306", 
            database_name="chinook"
        )
        self.user_request = "Sales per year"
        self.tables = ["customer", "invoice"]
        self.allowed_statements = ["SELECT"]

    @patch('builtins.input', side_effect=["test_user"])
    @patch('getpass.getpass', side_effect=["test_password"])
    def test_sql_agent_run(self, mock_input, mock_getpass):
        """Test SQL agent query execution"""
        sql_query = self.sql_agent.run(
            user_request=self.user_request,
            tables=self.tables,
            allowed_statements=self.allowed_statements
        )
        # Check that the query is not None or empty (simple assertion, can be expanded)
        self.assertIsNotNone(sql_query)
        self.assertTrue(len(sql_query) > 0, "The SQL query result should not be empty")

if __name__ == "__main__":
    unittest.main()
