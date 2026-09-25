from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

HF_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN") or os.getenv("HUGGINGFACE_API_KEY")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-Coder-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=HF_API_TOKEN,
)

model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("You : ")
    if user_input.strip().lower() == "exit":
        break
    result = model.invoke(user_input)
    print("AI : ", result.content)


