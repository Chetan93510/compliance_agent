# compliance_agent/main.py

import os
from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from parser_factory import get_parser

app = FastAPI()

# Allow frontend if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up templates
templates = Jinja2Templates(directory="templates")

# Ensure uploads dir exists
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload/", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file
    with open(file_location, "wb") as f:
        f.write(await file.read())

    try:
        # Get appropriate parser and extract text
        parser = get_parser(file_location)
        content = parser.parse(file_location)
    except Exception as e:
        content = f"❌ Error: {str(e)}"

    return templates.TemplateResponse("upload.html", {"request": request, "content": content})
