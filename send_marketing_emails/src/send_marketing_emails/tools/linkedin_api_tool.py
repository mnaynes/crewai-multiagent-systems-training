from typing import Type
from crewai_tools import BaseTool
from pydantic import BaseModel, Field
from linkedin_api import Linkedin
import os

class LinkedInAPIInput(BaseModel):
    """Input schema for LinkedInAPITool."""
    search_query: str = Field(..., description="Search query for LinkedIn")
    search_type: str = Field(default="content", description="Type of search: 'content', 'people', or 'companies'")
    max_results: int = Field(default=5, description="Maximum number of results to return")

class LinkedInAPITool(BaseTool):
    name: str = "LinkedIn API Tool"
    description: str = "A tool for searching LinkedIn using official API"
    args_schema: Type[BaseModel] = LinkedInAPIInput

    def __init__(self):
        super().__init__()
        # Get credentials from environment variables
        self.email = os.getenv('LINKEDIN_EMAIL')
        self.password = os.getenv('LINKEDIN_PASSWORD')
        if not self.email or not self.password:
            raise ValueError("LinkedIn credentials not found in environment variables")
        
        # Initialize LinkedIn API client
        self.api = Linkedin(self.email, self.password)

    def _run(self, search_query: str, search_type: str = "content", max_results: int = 5) -> str:
        try:
            results = []
            
            if search_type == "content":
                # Search for posts/content
                search_results = self.api.search_posts(search_query, limit=max_results)
                for post in search_results:
                    results.append({
                        'type': 'post',
                        'text': post.get('text', ''),
                        'author': post.get('author', ''),
                        'url': f"https://www.linkedin.com/feed/update/{post.get('updateUrn')}"
                    })

            elif search_type == "people":
                # Search for people
                search_results = self.api.search_people(search_query, limit=max_results)
                for person in search_results:
                    profile = self.api.get_profile(person['public_id'])
                    results.append({
                        'type': 'profile',
                        'name': profile.get('full_name', ''),
                        'headline': profile.get('headline', ''),
                        'location': profile.get('location', ''),
                        'url': f"https://www.linkedin.com/in/{person['public_id']}"
                    })

            elif search_type == "companies":
                # Search for companies
                search_results = self.api.search_companies(search_query, limit=max_results)
                for company in search_results:
                    results.append({
                        'type': 'company',
                        'name': company.get('name', ''),
                        'description': company.get('description', ''),
                        'url': f"https://www.linkedin.com/company/{company.get('universalName')}"
                    })

            if not results:
                return "No results found."

            # Format results
            formatted_results = []
            for idx, result in enumerate(results, 1):
                if result['type'] == 'post':
                    formatted_results.append(
                        f"Post {idx}:\n"
                        f"Author: {result['author']}\n"
                        f"Content: {result['text'][:300]}...\n"
                        f"URL: {result['url']}\n"
                    )
                elif result['type'] == 'profile':
                    formatted_results.append(
                        f"Profile {idx}:\n"
                        f"Name: {result['name']}\n"
                        f"Headline: {result['headline']}\n"
                        f"Location: {result['location']}\n"
                        f"URL: {result['url']}\n"
                    )
                else:  # company
                    formatted_results.append(
                        f"Company {idx}:\n"
                        f"Name: {result['name']}\n"
                        f"Description: {result['description'][:300]}...\n"
                        f"URL: {result['url']}\n"
                    )

            return "\n".join(formatted_results)

        except Exception as e:
            return f"Error performing LinkedIn search: {str(e)}" 