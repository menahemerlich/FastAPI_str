import json

from fastapi import FastAPI
from string_ops import reverse_str, to_upper

app = FastAPI()

@app.get("/reverse")
def reverse_app(text: str):
    result = json.dumps(reverse_str(text))
    return result

@app.get("/uppercase/{text}")
def uppercase(text):
    result = json.dumps(to_upper(text))
    return result
