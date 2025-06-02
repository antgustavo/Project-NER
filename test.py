from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3", temperature=0, base_url="http://192.168.133.192:11435")