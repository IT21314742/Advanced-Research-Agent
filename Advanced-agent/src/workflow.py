from typing import Dict, Any
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from .models import ResearchState, CompanyInfo, CompanyAnalysis
from .firecrawl import FirecrawlService
from .prompts import DeveloperToolsPrompts


class Workflow:
    def __init__(self):
        self.firecrawl = FirecrawlService()
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
        self.prompts = DeveloperToolsPrompts()
        self.workflow = self._build_workflow()
        
        
    def _build_workflow(self):
        graph = StateGraph(ResearchState)
        graph.add_node("extract_tools", self._extract_tools_step)
        graph.add_node("research", self._research_step)
        graph.add_node("analyze", self._analyze_step)
        graph.set_entry_point("extract_tools")
        graph.add_edge("extract_tools", "research")
        graph.add_edge("research", "analyze")
        graph.add_edge("analyze". END)
        return graph.compile()
    
    def _extract_tools_step(self, state: ResearchState) -> Dict[str, Any]:
        print(f"🔍 Finding articles about: {state.query}")
        
        
        
        article_query = f"{state.query} tools comparison best alternatives"
        search_results = self.firecrawl.search_companies(article_query, num_results=3)
        
        all_content = ""
        for result in search_results.data:
            