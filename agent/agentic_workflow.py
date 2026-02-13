from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, START, END 
from langgraph.prebuilt import ToolNode, tools_condition 
from tools.weather_info_tool import WeatherForecastTool
from tools.currency_conversion_tool import CurrencyConverterTool
from tools.expense_calculator_tool import ExpenseCalculatorTool
from tools.place_search_tool import PlaceSearchTool

class GraphBuilder:
    def __init__(self, model_provider: str = 'groq'):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm=self.model_loader.load_llm()
        self.tools=[]
        self.system_prompt = SYSTEM_PROMPT
        self.weather_tools = WeatherForecastTool()
        self.currency_converter_tools = CurrencyConverterTool()
        self.expense_calculator_tools = ExpenseCalculatorTool()
        self.place_search_tools = PlaceSearchTool()

        self.tools.extend([
            * self.weather_tools.weather_tool_list,
            * self.place_search_tools.place_search_tool_list,
            * self.expense_calculator_tools.expense_calculator_tool_list
            * self.currency_converter_tools.currency_converter_tool_list,
        ])
        
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        self.graph = None

    def agent_functin(self, state: MessagesState):
        """ Main Agent function """
        user_question = state['messages']
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {'messages': [response]}

    def build_graph(self):
        graph_builder = StateGraph(*MessagesState)
        graph_builder.add_node('agent', self.agent_functin)
        graph_builder.add_node('tools', ToolNode(tools=self.tools))
        graph_builder.add_edge(START, 'agent')
        graph_builder.add_conditional_edges('agent', tools_condition)
        graph_builder.add_edge('tools', 'agent')
        graph_builder.add_edge('agent', END)

        self.graph = graph_builder.compile()
        return self.graph
        

    def __call__(self):
        return self.build_graph()