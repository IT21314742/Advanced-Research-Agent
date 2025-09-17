class DeveloperToolPrompts:
    """Collection of prompts for analyzing developer tools and Technologies"""

    #Tool extraction prompts
    TOOL_EXTRACTION_SYSTEM = """You are a tech researcher Extract specific tool, library, platform or services names from articles.
                                 Focus on actual product/tools that developers can use, not general concepts or features."""
   
    @staticmethod
    def tool_extraction_user(query: str, content: str) -> str:
        return f"""Query: {query}
                 Article Content: {content}