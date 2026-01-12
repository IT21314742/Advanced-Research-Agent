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

