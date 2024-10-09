This project demonstrates the construction of a multi-agent system using IBM Cloud WatsonAI LLM, the CrewAI framework, and the Serper API. The system is designed to simulate the interaction between AI agents to complete specific tasks, such as conducting research and writing a keynote speech. The agents are customizable and can be adapted to various use cases, making this project a starting point for developing AI-driven workflows that require specialized task delegation.

## Features
- **Multi-Agent Architecture**: Uses multiple AI agents to perform different tasks in sequence.
  - **Research Agent**: Gathers research data from the web using WatsonAI and Serper API.
  - **Speech Writer Agent**: Generates engaging keynote speeches based on the research results.
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

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/multi-agent-system-watsonai.git
   cd multi-agent-system-watsonai
   ```

2. **Set up API keys**:
   - You will need your IBM Watsonx AI API key and Serper API key to run the agents.
   - Update the environment variables in `agent.py` or set them directly in your terminal:
     ```bash
     export WATSONX_APIKEY=<your-watsonx-api-key>
     export SERPER_API_KEY=<your-serper-api-key>
     ```

3. **Customize agents and tasks**:
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

## Project Structure

```
multi-agent-system-watsonai/
│
├── agent.py              # Main script that runs the multi-agent system
├── task1output.txt       # Output file for research agent
├── task2output.txt       # Output file for speech writer agent
└── README.md             # Project README
```

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

## License

This project is licensed under the MIT License.
