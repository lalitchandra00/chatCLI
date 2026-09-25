from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

import os

load_dotenv()

HF_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN") or os.getenv("HUGGINGFACE_API_KEY")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-Coder-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=HF_API_TOKEN,
)

model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content = "Ypu are a helpful assistant")
]


while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input.strip().lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("AI : ", result.content)

print(chat_history)



