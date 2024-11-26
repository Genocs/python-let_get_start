# Chat Model Documents: https://python.langchain.com/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/docs/integrations/chat/openai/
############################################################################################################
# This is a simple example of how to use the Langchain agent with a ChatOpenAI model.
# The agent is created with a ChatOpenAI model and a TavilySearchResults tool.
# You need to to have a Tavily API key to use the TavilySearchResults tool.
# You can get a Tavily API key by signing up at https://tavily.com/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage

from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# Create the agent
memory = MemorySaver()
search = TavilySearchResults(max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# Use the agent
config = {"configurable": {"thread_id": "abc123"}}

for chunk in agent_executor.stream(
    {"messages": [HumanMessage(
        content="Hi I am bob and I live in LA")]}, config
):
    print(chunk)
    print("----")

for chunk in agent_executor.stream(
    {"messages": [HumanMessage(
        content="Whats the weather where I live?")]}, config
):
    print(chunk)
    print("----")
