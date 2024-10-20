# LLM Task Agents

A collection of preset efficient prompts packaged into LLM agents.
LLM Task Agents is a Python package for creating and managing different agents that can handle tasks like image and text classification, SQL query generation, and JSON structure management. The agents are built on top of large language models (LLMs) and are designed to be modular and easy to integrate.

## Features

- **Text Classification Agent**: Classifies text into predefined categories using LLM-based prompts.
- **SQL Agent**: Runs SQL queries on databases and returns structured results.
- **JSON Agent**: Handles JSON validation and generation based on predefined schemas.
- **Image Classification Agent**: Classifies images into predefined categories using LLM models.
- **Graph Agent**: Generates graphs using LLM models for a given pandas DataFrame.

## Installation

### From PyPI

You can install the package via pip once it is uploaded to PyPI:

```bash
pip install llm-task-agents
```

## Usage

Below are examples of how to use the different agents provided by the package.

### Text Classification Agent

```python
from llm_task_agents.agent_factory import AgentFactory
import os
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax

# Initialize the console
console = Console()

# Text classification agent
text = "Je vois la vie en rose."

labels = ["Positive", "Negative"]

agent = AgentFactory.get_agent(
	 agent_type="text", 
	 llm_api_url=os.getenv("OLLAMA_API_BASE"), 
	 model="llama3.2:3b"
)

# Run the agent to classify text
result = agent.run(text=text, labels=labels)

# Display results
console.print("TEXT CLASSIFICATION AGENT")
console.print(f"[bold]Text:[/bold]\n{text}")
console.print(f"[bold]Labels:[/bold]\n{labels}")
console.print(f"[bold]Result:[/bold]\n{result}")
```

### SQL Agent

```python
from llm_task_agents.agent_factory import AgentFactory
import os
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax

# Initialize the console
console = Console()

# SQL Agent
user_request = "Show total sales per month"

agent = AgentFactory.get_agent(
    agent_type="sql",
    llm_api_url=os.getenv("OLLAMA_API_BASE"),
    model="llama3.2:3b",
    database_driver="mysql",
    database_username=os.getenv("MYSQL_USER", "root"),
    database_password=os.getenv("MYSQL_PASSWORD", "password"),
    database_host=os.getenv("MYSQL_HOST", "localhost"),
    database_port="3306",
    database_name="chinook",
    # debug=True,
)

# Get the list of tables
tables = agent.list_tables()

# Generate the SQL query
sql_query = agent.run(
    user_request=user_request,
    tables=tables,
    allowed_statements=["SELECT"]
)

# Function to display tables using rich Table
def display_tables(tables):
    table = Table(title="Database Tables")
    table.add_column("Table Name", justify="left", style="cyan", no_wrap=True)

    for table_name in tables:
        table.add_row(table_name)

    console.print(table)

# Display results
console.print("SQL AGENT")
display_tables(tables)
console.print(f"[bold]User Request:[/bold] {user_request}")

if sql_query:
    console.print("[bold green]Valid SQL Query:[/bold green]")
    syntax = Syntax(sql_query, "sql", theme="monokai", line_numbers=True)
    console.print(syntax)
else:
    console.print("[red]Failed to generate a valid SQL query.[/red]")
```

### JSON Agent

```python
from llm_task_agents.agent_factory import AgentFactory
import os
from rich.console import Console
import json

# Initialize the console
console = Console()

# JSON Agent
task = "Create 3 detailed, realistic character personas for a fantasy adventure game."

structure = {
    "personas": [
        {
            "first_name": "string", 
            "last_name": "string", 
            "age": "int", 
            "gender": "string", 
            "job": "string", 
            "description": "string"
        }
    ]
}

agent = AgentFactory.get_agent(
     agent_type="json", 
     llm_api_url=os.getenv("OLLAMA_API_BASE"), 
     model="llama3.2:3b"
)

# Run the agent to generate JSON
personas = agent.run(
    task=task,
    structure=structure
)

# Display results
console.print("JSON AGENT")
console.print(f"[bold]Task:[/bold]\n{task}")
console.print(f"[bold]Structure:[/bold]\n{json.dumps(structure, indent=4)}")
console.print(f"[bold]JSON:[/bold]\n{json.dumps(personas, indent=4)}")
```

### Image Classification Agent

```python
from llm_task_agents.agent_factory import AgentFactory
import os
from rich.console import Console
from PIL import Image
import requests
import tempfile

# Initialize the console
console = Console()

# Image classification agent
image_url = "https://image.pollinations.ai/prompt/Grape"
image = Image.open(requests.get(image_url, stream=True).raw)

# Create a temporary file
with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
    image.save(tmp_file.name)
    image_path = tmp_file.name

labels = ["Apple", "Lemon", "Cherry", "Orange", "Banana", "Pineapple", "Melon", "Watermelon", "Peach", "Grape"]

agent = AgentFactory.get_agent(
     agent_type="image", 
     llm_api_url=os.getenv("OLLAMA_API_BASE"), 
     model="minicpm-v:8b-2.6-fp16"
)

# Run the agent to classify image
label = agent.run(image_path=image_path, labels=labels)

# Display results
console.print("IMAGE CLASSIFICATION AGENT")
console.print(f"[bold]Image:[/bold]\n{image_path}")
console.print(f"[bold]Labels:[/bold]\n{labels}")
console.print(f"[bold]Result:[/bold]\n{label}")
```

### Graph Agent

```python
from llm_task_agents.agent_factory import AgentFactory
import os
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
import pandas as pd
import numpy as np
from PIL import Image
import io
import base64

# Initialize the console
console = Console()

# Generating a fake sales dataframe
np.random.seed(42)

# Creating a fake DataFrame with sales data
df_sales = pd.DataFrame({
	'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
	'Product': np.random.choice(['Product A', 'Product B', 'Product C'], size=100),
	'Region': np.random.choice(['North', 'South', 'East', 'West'], size=100),
	'Units Sold': np.random.randint(1, 100, size=100),
	'Price per Unit': np.random.uniform(5.0, 50.0, size=100),
	'Total Sales': lambda x: df_sales['Units Sold'] * df_sales['Price per Unit']
})

# Calculating total sales
df_sales['Total Sales'] = df_sales['Units Sold'] * df_sales['Price per Unit']

agent = AgentFactory.get_agent(
	 agent_type="graph", 
	 llm_api_url=os.getenv("OLLAMA_API_BASE"), 
	 model="llama3.2:3b"
)

# Run the agent to classify text
user_request = "Average Units Sold per Product",
img_base64, graph_title = agent.run(user_request=user_request, df=df)

# Display results
console.print("GRAPH AGENT")
console.print(f"[bold]User Request:[/bold]\n{user_request}")
console.print(f"[bold]Graph title:[/bold]\n{graph_title}")

# convert base64 to image
image = Image.open(io.BytesIO(base64.b64decode(img_base64)))

# display image
image.show()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using the `ollama` LLM API.
- SQL query management with SQLAlchemy.
- Graphs with plotly.
