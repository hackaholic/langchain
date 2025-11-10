from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
#from tavily import TavilyClient
from langchain_tavily import TavilySearch


load_dotenv()

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tools that searches over internet
    
#     Args:
#         query: The query to search
#     return:
#         The search result
#     """
#     print(f"searching for {query}")
#     #return "Tokyo weather is sunny"
#     return tavily.search(query=query)


@tool
def add_two_num(a:float, b:float) -> float:
    """
    This function take number and do addtion
    
    args:
        a: number one, float type
        b: number two, float type
        
    returns:
        number after addition of type float
    """
    
    print(f"add_two_num is called")
    return a+b

llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_tokens=None,
        max_retries=6,
        stop=None,
    )

tools = [TavilySearch(), add_two_num]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from ReaCT agent course!")
    #res = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo")})
    res = agent.invoke({"messages": HumanMessage(content="what is 9 + 6 ?")})
    print(res)
    


if __name__ == "__main__":
    main()