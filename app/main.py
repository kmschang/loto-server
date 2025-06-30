# app/main.py
import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
import json
from app.generate_pdf import create_pdf  # We'll add this wrapper

app = FastAPI()
TEMP_DIR = Path(__file__).parent / "temp"
TEMP_DIR.mkdir(exist_ok=True)

@app.post("/generate-pdf/")
async def generate_pdf(json_file: UploadFile = File(...), files: list[UploadFile] = File(...)):
    # Save uploaded files
    for f in files:
        file_path = TEMP_DIR / f.filename
        with open(file_path, "wb") as out_file:
            out_file.write(await f.read())

    # Save the uploaded JSON
    json_path = TEMP_DIR / json_file.filename
    with open(json_path, "wb") as out_file:
        out_file.write(await json_file.read())

    # Generate output PDF
    output_pdf_path = TEMP_DIR / f"{json_file.filename.rsplit('.', 1)[0]}.pdf"
    create_pdf(str(json_path), str(output_pdf_path))

    return FileResponse(output_pdf_path, media_type="application/pdf", filename=output_pdf_path.name)