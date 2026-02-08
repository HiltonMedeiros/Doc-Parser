# 📄 Doc-Parser: API de Extração de Dados via OCR

O **Doc-Parser** é uma API moderna e de alta performance desenvolvida para automatizar a extração de texto em documentos digitalizados. Utilizando o motor de OCR **Tesseract** e o framework **FastAPI**, o projeto é totalmente conteinerizado com **Docker**, garantindo que o ambiente de processamento seja idêntico em qualquer máquina (Windows, Linux ou Mac).

[Image of a sequence diagram: user uploads image to FastAPI, FastAPI calls Tesseract OCR engine inside Docker, engine returns text to FastAPI, and FastAPI returns JSON to user]

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**: Linguagem base do projeto.
* **FastAPI**: Framework web focado em performance e tipagem.
* **Docker**: Isolamento do ambiente e gerenciamento de dependências do sistema.
* **Tesseract OCR**: Motor de reconhecimento óptico de caracteres open-source.
* **Pillow (PIL)**: Biblioteca para manipulação e pré-processamento de imagens.

## 🛠️ Como Executar o Projeto

Graças ao Docker, você não precisa configurar o Tesseract no seu sistema operacional. Tudo o que você precisa é do Docker Desktop instalado.


No terminal, dentro da pasta raiz do projeto, execute:
```bash
docker build -t doc-parser-image .

### 2. Rodar o Container:
```bash
docker run -d -p 8000:8000 --name meu-parser doc-parser-image

### 3. Testar a API

Abra o navegador e acesse a documentação interativa (Swagger UI): 👉 http://localhost:8000/docs