from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage

load_dotenv()

@tool
def search(query: str) -> str:
    """
    Tools that searches over internet
    
    Args:
        query: The query to search
    return:
        The search result
    """
    print(f"searching for {query}")
    return "Tokyo weather is sunny"


llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_tokens=None,
        max_retries=6,
        stop=None,
    )

tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from ReaCT agent course!")
    res = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo")})
    print(res)
    


if __name__ == "__main__":
    main()