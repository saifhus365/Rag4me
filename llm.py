import requests


llm = requests.get("https://llm.srv.webis.de/api/generate")
print(llm.content)