from fastapi import FastAPI, UploadFile, File, HTTPException
from app.services.ocr_engine import OCRService

app = FastAPI(
    title="Doc-Parser API",
    description="API para extração de texto de documentos usando OCR",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Doc-Parser está online e operante!"}

@app.post("/v1/extract")
async def extract_document_text(file: UploadFile = File(...)):
    # Verificação simples de extensão
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O arquivo enviado deve ser uma imagem.")

    # Lê os bytes do arquivo enviado
    contents = await file.read()
    
    # Chama o serviço de OCR
    extracted_text = OCRService.extract_text(contents)
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "text": extracted_text
    }