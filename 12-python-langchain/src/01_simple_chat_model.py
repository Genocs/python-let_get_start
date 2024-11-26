# Chat Model Documents: https://python.langchain.com/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/docs/integrations/chat/openai/
############################################################################################################
# This script demonstrates how to create a simple chat model using the LangChain OpenAI Chat Model.



from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")

# Print the result
print("Full result:")
print(result)
print("Content only:")
print(result.content)
