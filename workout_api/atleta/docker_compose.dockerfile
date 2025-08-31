# Base Python
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /code

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Expor porta da API
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "workout_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
