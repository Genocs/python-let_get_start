# Chat Model Documents: https://python.langchain.com/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/docs/integrations/chat/openai/
############################################################################################################
# This script demonstrates how to create a simple chat model using the LangChain OpenAI Chat Model.
# The script uses a ChatPromptTemplate to create a chat model that translates a message from English into a specified language.

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# result = prompt_template.invoke({"language": "Italian", "text": "hi!"})
# print("Result:")
# print(result.to_messages())

chain = prompt_template | model

# Invoke the model with a message
response = chain.invoke({"language": "Italiano", "text": "hi!"})

# Print the result
print(response.content)
