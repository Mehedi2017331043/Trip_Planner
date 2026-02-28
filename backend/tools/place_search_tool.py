import os 
from utils.place_search import TavilyPlaceSearch
from dotenv import load_dotenv
from langchain.tools import tool 
from typing import List 

class PlaceSearchTool:
    def __init__(self):
        self.tavily_api_key = os.environ.get('TAVILY_API_KEY')
        self.tavily_search = TavilyPlaceSearch(api_key=self.tavily_api_key)
        self.place_search_tool_list = self._setup_tools()
    
    def _setup_tools(self) -> List:
        """ Setup all tools for the place search tool"""
        @tool
        def search_attrations(place: str) -> str:
            """Search attractions of a place"""

            try:
                attraction_result = self.tavily_search.tavily_search_attractions(place=place)
                return f"\nFollowing are the attraction of {place}: {attraction_result}"
            
            except Exception as e:
                print(e)
                return f"Could not featch weather fro {place}"
        
        @tool
        def search_restaurents(place: str) -> str:
            """Search famous restaurents around of a place"""
            try:
                attraction_result = self.tavily_search.tavily_search_restaurants(place=place)
                return f"\nFollowing are the famous restaurents of {place}: {attraction_result}"
            
            except Exception as e:
                print(e)
                return f"Could not featch weather fro {place}"
            
        @tool
        def search_activities(place: str) -> str:
            """Search activites around of a place"""
            try:
                attraction_result = self.tavily_search.tavily_search_activity(place=place)
                return f"\nFollowing are the activities of {place}: {attraction_result}"
            
            except Exception as e:
                print(e)
                return f"Could not featch weather fro {place}"
            
        @tool
        def search_tansportation(place: str) -> str:
            """Search transportations around of a place"""
            try:
                attraction_result = self.tavily_search.tavily_search_transportation(place=place)
                return f"\nFollowing are the transportations arround of {place}: {attraction_result}"
            
            except Exception as e:
                print(e)
                return f"Could not featch weather fro {place}"
        
        return [search_attrations, search_restaurents, search_activities, search_tansportation]

            