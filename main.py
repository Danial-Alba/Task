from fastapi import FastAPI, File, UploadFile
from openpyxl import load_workbook
import shutil
import os

app = FastAPI()

@app.post("/upload_excel/")
async def upload_excel(file: UploadFile = File(...)):
   
   
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

   
   
    workbook = load_workbook(file_location)

   
   
    os.remove(file_location)
    
    return {"filename": file.filename}
