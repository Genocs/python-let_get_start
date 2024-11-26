# Chat Model Documents: https://python.langchain.com/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/docs/integrations/chat/openai/
############################################################################################################
# This script demonstrates how to create a simple chat model using the LangChain OpenAI Chat Model.

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# Invoke the model with a message
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

# Invoke the model with a message
result = model.invoke(messages)

# Print the result
print("Result is:")
print(result.content)
