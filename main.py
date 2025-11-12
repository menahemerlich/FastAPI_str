from fastapi import FastAPI
from string_ops import reverse_str

app = FastAPI()

@app.get("/reverse")
def reverse_app(text: str):
    result = reverse_str(text)
    return result

