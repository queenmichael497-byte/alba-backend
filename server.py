from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from groq import Groq

app = FastAPI(title="Alba AI Backend")

# Allow your frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. PUT YOUR GROQ KEY HERE
GROQ_API_KEY = "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" 
client = Groq(api_key=GROQ_API_KEY)

class Message(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Alba AI Backend is Live 🇳🇬"}

@app.post("/chat")
async def chat(msg: Message):
    user_message = msg.message
    
    try:
        # Call Groq and force it to speak Naija Pidgin
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant", # Fast + Free
            messages=[
                {
                    "role": "system", 
                    "content": "You are Alba, a helpful AI assistant from Nigeria. Always reply in Nigerian Pidgin. Be friendly, funny, and helpful. Use words like 'wahala', 'how far', 'na so'."
                },
                {"role": "user", "content": user_message}
            ],
            temperature=0.8,
            max_tokens=300,
        )
        
        reply = completion.choices[0].message.content
        return {"reply": reply}
        
    except Exception as e:
        return {"reply": f"Wahala dey o: {str(e)}"}
