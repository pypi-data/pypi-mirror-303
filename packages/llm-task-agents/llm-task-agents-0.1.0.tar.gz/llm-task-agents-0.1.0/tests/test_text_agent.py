import os
import unittest
from llm_task_agents.agent_factory import AgentFactory  # Absolute import based on package structure

class TestTextClassificationAgent(unittest.TestCase):

    def setUp(self):
        """Set up the environment and agent for testing"""
        self.llm_api_url = os.getenv("OLLAMA_API_BASE")
        self.text_agent = AgentFactory.get_agent(
            agent_type="text", 
            llm_api_url=self.llm_api_url, 
            model="llama3.2:3b"
        )
        self.text = "Vous n’êtes pas du tout semblables à ma rose, vous n’êtes rien encore, leur dit-il. Personne ne vous a apprivoisées et vous n’avez apprivoisé personne. Vous êtes comme était mon renard. Ce n’était qu’un renard semblable à cent mille autres. Mais j’en ai fait mon ami, et il est maintenant unique au monde."
        self.labels = ["Happy", "Sad", "Angry", "Fearful", "Surprised", "Disgusted", "Neutral"]

    def test_text_classification(self):
        """Test text classification functionality"""
        label = self.text_agent.run(
            text=self.text, 
            labels=self.labels
        )
        self.assertIn(label, self.labels, f"Returned label '{label}' is not in the expected labels")

if __name__ == "__main__":
    unittest.main()
