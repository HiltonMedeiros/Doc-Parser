import pytesseract
from PIL import Image
import io

class OCRService:
    @staticmethod
    def extract_text(image_bytes: bytes) -> str:
        """
        Recebe os bytes de uma imagem e retorna o texto extraído.
        """
        try:
            # 1. Converte os bytes recebidos via API para um objeto de Imagem
            image = Image.open(io.BytesIO(image_bytes))

            # 2. Pré-processamento básico:
            # Convertemos para escala de cinza ('L') para facilitar a leitura do OCR
            image = image.convert("L")

            # 3. Chama o Tesseract para extrair o texto
            # 'lang=por' indica que ele deve buscar caracteres da língua portuguesa
            text = pytesseract.image_to_string(image, lang='por')

            return text.strip()
        
        except Exception as e:
            return f"Erro ao processar a imagem: {str(e)}"