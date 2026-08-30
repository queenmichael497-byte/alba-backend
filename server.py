from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from naijalingo_asr import transcribe
import shutil, uuid, os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def home():
    return {"message": "Alba AI Backend is Live"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile, language: str = Form("yo")):
    file_id = f"{uuid.uuid4()}.wav"
    with open(file_id, "wb") as buffer: shutil.copyfileobj(file.file, buffer)
    text = transcribe(file_id, language=language)
    os.remove(file_id)
    return {"text": text, "language": language}
