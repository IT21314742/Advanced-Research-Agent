class DeveloperToolPrompts:
    """Collection of prompts for analyzing developer tools and Technologies"""

    #Tool extraction prompts
    TOOL_EXTRACTION_SYSTEM = """You are a tech researcher Extract specific tool, library, platform or services names from articles.
                                 Focus on actual product/tools that developers can use, not general concepts or features."""
   
    @staticmethod
    def tool_extraction_user(query: str, content: str) -> str:
        return f"""Query: {query}
                 Article Content: {content}

                    Extract a list of specific tool/service names mentioned in this content that are relevent to "{query}"

                    Rules:
                    - Only include actual product names, not generic terms.
                    - Focus on tools developers can directly use/implement.
                    - Include both open source and commercial options.
                    - Limit to the 5 most relevent tools.
                    - Return just the tool names, one per line, no descriptions.

                    Example format:
                    superbase
                    PlanetScale
                    Railway
                    Appwrite
                    Nhost"""
    

    # Company/Tool Analysis prompts
    TOOL_ANALYSIS_SYSTEM = """You are analyzing developer tools and programming technologies.
                           focus on extracting information relevent to programmers and software developers.
                           Pay special attention to programming languages, frameworks, APIs, SDKs, and development workflows."""
    
    @staticmethod
    def tool_analysis_user(query: str, content: str) -> str:
        return f"""Query: {query}
                Article Content: {content}
                
                Extract a list of specific tool/service names mentioned in this content that are relevent to "{query}".
                
                Rules:
                - Only include actual product names, not generic terms
                - Focus on tools developers can directly use/implement
                - Include both open source and commercial options
                - Limit to the 5 most relevent tools
                - Return just the tool names, one per line, no descriptions
                
                
                Example format:
                Superbase
                PlanetScale
                Railway
                Appwrite
                Nhost"""
    

    #Company/Tool Analysis Prompts
    TOOL_ANALYSIS_SYSTEM = """You are analyzing tools and programming technologies.
                            focus on actual products/tools that developers can use, not general concepts or features."""
    
    @staticmethod
    def tool_analysis_user(company_name: str, content: str) -> str:
        return f"""Company/Tool: {company_name}
                Website Content: {content[:2500]}

                Analyze this content from a developer's perspective and provide:
                - pricing_model: One of "Free", "Freemium", "Paid", "Enterprise", or "Unknown"
                - is_open_source: true if open source, false if proprietary, null if unclear
                - tech_stack: List of programming languages, frameworks, databases
                - description: Brief 1-sentence