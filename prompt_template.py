# This is not  used in this porject
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# Chat Template
chat_template = ChatPromptTemplate([
    ('system',  'You are a good AI helper'),
    # this will bring chat history from a seperate file called chat-history
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human' '{query}')
])

chat_history_here = []
with open('chat_history.txt') as file:
    chat_history_here.extent(file.readlines())

# Final Prompt which will be sent to llm
final_prompt = chat_template.invoke({"chat_history" : chat_history_here, 'query' : "where is my refund"})