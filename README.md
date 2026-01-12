# Advanced Research Agent

Advanced Research Agent is a Python-based autonomous research system that uses Large Language Models (LLMs), the Model Context Protocol (MCP), and Firecrawl to perform intelligent web research.

The project demonstrates the evolution from a simple interactive agent into a structured, workflow-driven research agent capable of crawling websites, extracting information, and returning structured research results.

---

## 🎯 Project Goals

- Build a practical autonomous research agent
- Integrate Firecrawl MCP tools for real-world web data extraction
- Apply ReAct-style LLM reasoning for tool usage
- Transition from a single-agent prototype to a scalable workflow architecture
- Produce structured, comparable research outputs

---

## 🧠 How the Project Works

The system operates in two stages:

### 1. Simple Research Agent

The initial agent is a single ReAct-based LLM agent that:

- Connects to Firecrawl via MCP
- Dynamically loads available crawling and scraping tools
- Uses step-by-step reasoning to decide which tools to call
- Runs in an interactive command-line interface

This stage focuses on experimentation, tool discovery, and validating MCP-based tool execution.

---

### 2. Advanced Research Agent

The advanced agent introduces a **Workflow layer** that orchestrates research execution.

Key responsibilities of the workflow include:

- Accepting user research queries
- Guiding the LLM through structured research steps
- Executing Firecrawl-powered crawling and extraction
- Normalizing raw data into structured entities
- Returning organized research results (e.g., companies and tools)

This design separates reasoning, execution, and output processing, making the system easier to extend and maintain.

---


## 🏗️ System Architecture Overview

At a high level, the system consists of:

- A CLI-based user interface
- A workflow orchestration layer
- An LLM reasoning agent (LangGraph ReAct)
- MCP client communication
- Firecrawl MCP server for web crawling and scraping
- Result processing and structured output

A full system architecture diagram is provided separately.

---


## 🛠️ Technology Stack

- **Python 3.10+**
- **LangChain**
- **LangGraph**
- **Model Context Protocol (MCP)**
- **Firecrawl API**
- **OpenAI GPT-4o-mini**
- **AsyncIO**
- **python-dotenv**

---


## 📁 Project Structure (High Level)

```text
.
├── simple_agent.py          # Prototype MCP research agent
├── main.py                  # Advanced research agent entry point
├── src/
│   └── workflow.py          # Research workflow orchestration
├── .env.example
├── requirements.txt
└── README.md
```

## 📦 Installation

Clone the repository:

- git clone https://github.com/IT21314742/Advanced-Research-Agent.git
- cd Advanced-Research-Agent


## Install dependencies:

```
pip install -r requirements.txt
```


## Create a .env file and add your API keys:
```
 OPENAI_API_KEY=your_openai_key
 FIRECRAWL_API_KEY=your_firecrawl_key
```

## ▶️ Usage

### Run the Simple Agent
```
python simple_agent.py
```

- Interactive research session
- Direct tool usage via MCP
- Ideal for experimentation


### Run the Advanced Research Agent
```
python main.py
```
You will be prompted to enter a research query, for example:

*AI developer tools for code review*


### The agent will return structured research results such as:

- Tool or company name
- Official website
- Pricing model
- Open-source availability
- Technology stack (when available)


## 📊 Example Output
1. ExampleTool
   - Website: https://example.com
   - Pricing: Freemium
   - Open Source: No
   - Tech Stack: Python, FastAPI, React


## 🧱 Extending the System

#### The architecture is designed for extension. Possible improvements include:

- Adding additional workflow stages

- Supporting new research domains

- Exporting results to JSON, CSV, or Markdown

- Adding memory or caching layers

- Parallelizing research tasks


## 🧭 Roadmap

 - Persistent memory

 - Citation and source tracking

 - Parallel research execution

 - Report generation

 - Web or API interface


## 🤝 Contributing

* Contributions, issues, and ideas are welcome.
This project is intended for developers interested in LLM agents, autonomous research systems, and MCP-based tooling. *
