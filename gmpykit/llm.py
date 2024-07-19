import requests
import json

ollama_url = 'http://localhost:11434/api/generate'
ollama_llm_name = 'llama3'

def init(url:str, llm_name: str):
    global ollama_url, ollama_llm_name
    ollama_url = url
    ollama_llm_name = llm_name


def ask(prompt):
    global ollama_url, ollama_llm_name
    response = requests.post(ollama_url, json={'model': ollama_llm_name, 'prompt': prompt, 'option': {'temperature': 0}})
    text = response.text.strip()
    lines = text.split('\n')
    tokens = list(map(lambda line: json.loads(line)['response'], lines))
    formated = ''.join(tokens)
    answer = formated.strip()
    return answer
