from .agents.image_classification_agent import ImageClassificationAgent
from .agents.text_classification_agent import TextClassificationAgent
from .agents.sql_agent import SQLAgent
from .agents.json_agent import JSONAgent
from .agents.graph_agent import GraphAgent
from .agents.subtasks_agent import SubTasksAgent

class AgentFactory:
	@staticmethod
	def get_agent(agent_type, **kwargs):
		if agent_type == "image":
			return ImageClassificationAgent(
				llm_api_url=kwargs['llm_api_url'], 
				model=kwargs['model'], 
				debug=kwargs.get('debug', False)
			)
		elif agent_type == "text":
			return TextClassificationAgent(
				llm_api_url=kwargs['llm_api_url'], 
				model=kwargs['model'], 
				debug=kwargs.get('debug', False)
			)
		elif agent_type == "sql":
			return SQLAgent(
				llm_api_url=kwargs['llm_api_url'], 
				model=kwargs['model'], 
				database_driver=kwargs['database_driver'],
				database_username=kwargs['database_username'],
				database_password=kwargs['database_password'],
				database_host=kwargs['database_host'],
				database_port=kwargs['database_port'],
				database_name=kwargs['database_name'],
				debug=kwargs.get('debug', False)
			)
		elif agent_type == "json":
			return JSONAgent(
				llm_api_url=kwargs['llm_api_url'], 
				model=kwargs['model'], 
				debug=kwargs.get('debug', False)
			)
		elif agent_type == "graph":
			return GraphAgent(
				llm_api_url=kwargs['llm_api_url'], 
				model=kwargs['model'], 
				debug=kwargs.get('debug', False)
			)
		elif agent_type == "subtasks":
			return SubTasksAgent(
				llm_api_url=kwargs['llm_api_url'], 
				model=kwargs['model'], 
				database_driver=kwargs['database_driver'],
				database_username=kwargs['database_username'],
				database_password=kwargs['database_password'],
				database_host=kwargs['database_host'],
				database_port=kwargs['database_port'],
				database_name=kwargs['database_name'],
				debug=kwargs.get('debug', False)
			)
		else:
			raise ValueError(f"Unknown agent type: {agent_type}")
