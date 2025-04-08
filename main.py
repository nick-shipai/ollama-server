from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

# 🔓 Allow all websites to access this backend (CORS fix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or just ["http://127.0.0.1:5500"] if you want to be strict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/generate")
async def generate(request: Request):
    body = await request.json()
    model = body.get("model", "tinyllama")
    prompt = body.get("prompt", "")

    result = subprocess.run(
        ["ollama", "run", model, prompt],
        capture_output=True,
        text=True
    )

    return {"response": result.stdout}
