User Query (CLI)
       │
       ▼
┌─────────────────────┐
│   Workflow Engine   │
│ (src/workflow.py)   │
└─────────────────────┘
       │
       ▼
┌────────────────────────────┐
│  LLM Reasoning Layer        │
│  (LangGraph ReAct Agent)    │
└────────────────────────────┘
       │
       ▼
┌────────────────────────────┐
│  Firecrawl MCP Tools        │
│  - Crawl Websites           │
│  - Scrape Pages             │
│  - Extract Structured Data  │
└────────────────────────────┘
       │
       ▼
┌────────────────────────────┐
│   Result Processing         │
│   - Company Models          │
│   - Pricing / Stack         │
└────────────────────────────┘
       │
       ▼
Structured Research Output
