# ChatCLI

A simple CLI chatbot built with LangChain and HuggingFace's Qwen2.5-Coder-7B-Instruct model.

## Features

- Interactive CLI chat with conversation history
- Uses HuggingFace Inference API
- Built with LangChain

## Setup

1. **Clone the repo**
```bash
git clone <repo-url>
cd chatCLI
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
```
Add your HuggingFace API key to `.env` (get it from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)).

4. **Run the chatbot**
```bash
python chatbot.py
```

## Usage

- Type your message and press Enter
- Type `exit` to end the conversation
- The full chat history is printed at the end

## Notes

- The model used is `Qwen/Qwen2.5-Coder-7B-Instruct` via HuggingFaceEndpoint
- Supports both `HUGGINGFACE_API_KEY` and `HUGGINGFACEHUB_API_TOKEN` env vars
- `prompt_template.py` contains an unused chat template example
