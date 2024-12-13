import requests

from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/')
def home():
    return {"hello" : "World"}

@app.get('/ask')
def ask(prompt :str):
    res = requests.post('http://ollama:11434/api/generate', json={
        "prompt": prompt,
        "stream" : False,
        "model" : "llama3.3:70b"
    })

    return Response(content=res.text, media_type="application/json")


# from fastapi import FastAPI, Response
# import httpx

# app = FastAPI()

# @app.get('/ask')
# async def ask(prompt: str):
#     async with httpx.AsyncClient() as client:
#         response = await client.post('http://ollama:11434/api/generate', json={
#             "prompt": prompt,
#             "stream": False,
#             "model": "llama3.3:70b"
#         })
#     return Response(content=response.text, media_type="application/json")
