from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class CompanyAnalysis(BaseModel):
    """Structured output for LLM company analysis focused on developer tools"""
    pricing_model: str #Free, Premium, Paid, Enterprise, Unknown
    is_open_source: Optional[bool] = None
    tech_stack: List[str] = []
    description: str=""
    api_available: Optional[bool] = None
    language_support: List[str] = []
    intergration_capabilities: List[str] = []