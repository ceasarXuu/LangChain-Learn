from langchain_mistralai.chat_models import ChatMistralAI
from langchain.schema import HumanMessage

# chat = ChatMistralAI()
chat = ChatMistralAI(token="your_bearer_token_here")

messages = [
    HumanMessage(content="Hello, how can I assist you?")
]

response = chat.invoke(messages)
print(response.content)