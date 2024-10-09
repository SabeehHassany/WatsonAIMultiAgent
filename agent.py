# agent.py
# This script is designed to demonstrate the construction of a multi-agent system using 
# IBM Cloud WatsonAI LLM, the CrewAI framework, and Serper API. The system is based on 
# multiple AI agents interacting to complete specific tasks, such as a researcher and a
# keynote speech writer. This can be customed and adjusted for a specific use-case.

from crewai import Crew, Task, Agent  # Importing the core components from crewAI to create agents, tasks, and crew
from crewai_tools import SerperDevTool  # Importing a tool to enable the agent to perform web searches
from langchain_ibm import WatsonxLLM  # Importing IBM Watson LLM interface to interact with Watsonx AI models
import os
import sys
# sys.setrecursionlimit(200)  # Adjusting recursion limit temporarily, commented out since it's not required here

# Set API keys using environment variables for Watsonx and SerperDevTool
os.environ["WATSONX_APIKEY"] = "lAKK1dN9lChkb0QskjI85oFrAVySCusAKv3QFduMZG25"  # Watsonx API key to access Watson AI services
os.environ["SERPER_API_KEY"] = "<a448486a6f2db6663fc63e8a82fc60bfd1017101>"  # API key for Serper Dev Tool to enable web searches

# Parameters for the language model, including decoding method and max tokens (limit output length)
parameters = {"decoding_method": "greedy", "max_new_tokens": 500}

# Create the first language model (LLM) for general tasks, using Watsonx AI's Llama 3 model
llm = WatsonxLLM(
    model_id="meta-llama/llama-3-70b-instruct",  # Using Meta's Llama 3 model for general-purpose text generation
    url="https://us-south.ml.cloud.ibm.com",  # URL endpoint to access Watsonx AI services
    params=parameters,  # Parameters like decoding method and token limits
    project_id="853780be-1a79-4185-8642-bbd8370910fd",  # Project ID to isolate and manage the tasks in Watsonx
)

# Uncomment to test the LLM with a sample prompt
# print(llm.invoke('who is Niels Bohr?'))  # Example to test the LLM invocation, asking about Niels Bohr

# Create the second LLM dedicated for function calling, using Watsonx AI's Granite model
function_calling_llm = WatsonxLLM(
    model_id="ibm/granite-13b-instruct-v2",  # A different model (Granite) for function-specific tasks
    url="https://us-south.ml.cloud.ibm.com",  # URL endpoint to access Watsonx AI services
    params=parameters,  # Parameters such as token limits and decoding
    project_id="853780be-1a79-4185-8642-bbd8370910fd",  # Project ID to manage specific tasks
)

# Initialize the tool that allows agents to search the internet
search = SerperDevTool()  # Tool that enables the agent to query the web using Serper's API

# Create the first agent, which will act as a researcher
researcher = Agent(
    llm=llm,  # Assign the Llama model to this agent for general-purpose generation
    function_calling_llm=function_calling_llm,  # Assign the function-specific LLM for advanced tasks
    role="Senior AI Researcher",  # Define the role of the agent
    goal="Find promising research in the field of quantum computing.",  # The task this agent focuses on
    backstory="You are a veteran quantum computing researcher with a background in modern physics.",  # Agent's background to give it personality/context
    allow_delegation=False,  # Disallow delegation for this agent (meaning it won’t pass tasks to other agents)
    tools=[search],  # Equip the agent with the SerperDevTool for web searches
    verbose=1,  # Enable detailed logging for this agent
)

# Define the first task for the researcher agent
task1 = Task(
    description="Search the internet and find 5 examples of promising AI research.",  # Task description
    expected_output="A detailed bullet point summary on each of the topics. Each bullet point should cover the topic, background and why the innovation is useful.",  # Expected task output
    output_file="task1output.txt",  # Output file where the results will be saved
    agent=researcher,  # Assign the researcher agent to complete this task
)

# Create the second agent, which will write a speech based on the research
writer = Agent(
    llm=llm,  # Reuse the general-purpose Llama model for text generation
    role="Senior Speech Writer",  # Define the role of this agent as a speech writer
    goal="Write engaging and witty keynote speeches from provided research.",  # Task for this agent to create speeches based on research
    backstory="You are a veteran quantum computing writer with a background in modern physics.",  # Backstory to provide context and personality to the agent
    allow_delegation=False,  # Disallow delegation for this agent
    verbose=1,  # Enable detailed logging for this agent
)

# Define the second task for the speech-writing agent
task2 = Task(
    description="Write an engaging keynote speech on quantum computing.",  # Task description for writing a keynote speech
    expected_output="A detailed keynote speech with an intro, body and conclusion.",  # Structure of the expected output
    output_file="task2output.txt",  # Output file for the completed speech
    agent=writer,  # Assign the speech writer agent to complete this task
)

# Combine agents and tasks into a Crew, which manages the flow and execution of tasks
crew = Crew(agents=[researcher, writer], tasks=[task1, task2], verbose=1)  # Crew combines agents and tasks, enabling them to execute in sequence
print(crew.kickoff())  # Start the process and print the result when complete