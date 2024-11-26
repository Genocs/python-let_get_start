# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain_core.tools import tool

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


# Invoke the model with a message
response = multiply.invoke({"a": 2, "b": 3})

print(multiply.name)  # multiply
print(multiply.description)  # Multiply two numbers.
print(multiply.args)

print(response)
