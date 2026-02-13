from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GoogleGeocodingAPIWrapper

class GooglePlaceSearch:
    def __init__(self, api_key: str):
        self.places_wrapper = GoogleGeocodingAPIWrapper(google_api_key=api_key)
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)

    def google_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using GooglePlaces API
        """
        return self.places_tool.run(f"Top attractive places in and around {place}")
    
    def google_search_restaurants(self, place: str) -> dict:
        """ 
        Searches for available restaurents in the specified place using GooglePlace API 
        """
        return self.places_tool.run(f"What are the top 10 restaurents and eateries in and around {place}")
    
    def google_search_activity(self, place: str) -> dict:
        """ 
        Searches for popular available activities around the specified place using GooglePlace API 
        """
        return self.places_tool.run(f"Popular activities in and around {place}")
    
    def google_search_transportation(self, place: str) -> dict:
        """ 
        Searches for available modes of transportation in the specified place using GooglePlaces API 
        """
        return self.places_tool.run(f'What are the different modes of transportations available in {place}')
    

class TavilyPlaceSearch:
    def __init__(self, api_key: str):
        self.tavily_api_key = api_key

    def tavily_search_attractions(self, place: str) -> dict:
        """ Searches for attractions in the specified place using TravilySearch"""
        tavily_tool = TavilySearch(
            tavily_api_key=self.tavily_api_key, 
            topic='general', 
            include_answer='advanced'
        )
        result = tavily_tool.invoke({'query': f"Top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get('answer'):
            return result['answer']
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """ Searches for available restaurents in the specified place using TavilySearch."""
        tavily_tool = TavilySearch(
            tavily_api_key=self.tavily_api_key, 
            topic='general', 
            include_answer='advanced'
        )
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(
            tavily_api_key=self.tavily_api_key,
            topic="general", 
            include_answer="advanced"
        )
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(
            tavily_api_key=self.tavily_api_key,
            topic="general", 
            include_answer="advanced"
        )
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result