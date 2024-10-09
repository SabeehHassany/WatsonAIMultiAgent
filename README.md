# Multi Agent LLM System using WatsonAI

This project is a simple but powrful demonstration of a multi-agent system using IBM Cloud WatsonAI LLM, the CrewAI framework, and the Serper API. The system is designed to simulate the interaction between AI agents to complete specific tasks, such as conducting research and writing a keynote speech. The agents are customizable and can be adapted to various use cases, making this project a starting point for developing AI-driven workflows that require specialized task delegation.


## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Running the Script](#running-the-script)
- [Output](#output)
- [Customization](#customization)
  - [Example](#example)
- [Future Directions](#future-directions)

## Features
- **Multi-Agent Architecture**: Uses multiple AI agents to perform different tasks in sequence.
- **WatsonAI Integration**: Leverages IBM Watsonx LLM for natural language processing and generation.
- **CrewAI Framework**: Manages the agents, tasks, and overall workflow execution.
- **Serper API**: Allows agents to search the web for real-time data.
- **Modular Design**: Agents and tasks can be easily customized for different purposes.

## Getting Started

### Prerequisites
- **Python 3.8+**
- **IBM Cloud Account** for accessing WatsonAI services.
- **Serper API Key** (available at [Serper.dev](https://serper.dev/)).
- The following Python libraries are required:
  - `crewai`
  - `langchain_ibm`
  - `serper`

Install the dependencies with:
```bash
pip install crewai langchain_ibm serper
```

### Setup

1. **Set up API keys**:
   - You will need your IBM Watsonx AI API key and Serper API key to run the agents.
   - Update the environment variables in `agent.py` or set them directly in your terminal:
     ```bash
     export WATSONX_APIKEY=<your-watsonx-api-key>
     export SERPER_API_KEY=<your-serper-api-key>
     ```

2. **Customize agents and tasks**:
   - Modify the agents’ goals and tasks in `agent.py` to match your specific use case.
   - You can customize the LLM models by changing the model IDs and the roles of agents.

### Running the Script

Run the script using Python:
```bash
python agent.py
```

This will initiate the multi-agent system, where the first agent will gather research from the web, and the second agent will generate a keynote speech based on the research.

### Output

- **Task Outputs**: 
  - The research findings will be saved in `task1output.txt`.
  - The generated keynote speech will be saved in `task2output.txt`.

## Customization

You can expand or modify this project by:
- Adding new agents for different tasks (e.g., a summary agent or a report generator).
- Using different LLM models from IBM WatsonAI to improve or alter the results.
- Modifying tasks to perform different types of research or writing tasks.

### Example

To create an additional agent for summarizing data, you can add a new `Agent` instance to the script and assign it a task using the CrewAI framework.

```python
# Example new agent
summarizer = Agent(
    llm=llm,
    role="Data Summarizer",
    goal="Summarize research data in a concise manner.",
    backstory="You are an experienced data analyst with a focus on summarization.",
    verbose=1,
)

# Example new task
task3 = Task(
    description="Summarize the research data collected by the Research Agent.",
    expected_output="A concise summary of the research data.",
    output_file="task3output.txt",
    agent=summarizer,
)
```
## Future Directions

- Implement agent-to-agent delegation to allow more complex task handoffs between agents.
- Expand the system by adding agents with new specialized roles, such as data analysts, summarizers, or content editors.
- Incorporate additional APIs such as GitHub, Google Drive, or custom data sources to create workflow connectivity.
- Upgrade to newer, more powerful IBM language models for better performance
