from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class CompanyAnalysis(BaseModel):
    """Structured output for LLM company analysis focused on developer tools"""
    pricing_model: str #Free, Premium, Paid, Enterprise, Unknown
    