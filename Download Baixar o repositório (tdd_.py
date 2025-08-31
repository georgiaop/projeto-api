Download: Baixar o repositório (tdd_fastapi_mongo.zip)

O que está dentro do .zip

app/ — aplicação FastAPI completa (main.py, database.py, models.py, routes/items.py)

tests/ — teste de exemplo com pytest (tests/test_items.py)

requirements.txt

docker-compose.yml — para subir o MongoDB (imagem oficial)

sample_db_dump.json — dados de exemplo que você pode importar com mongoimport

postman_collection.json — coleção Postman simples (modelo)

figma_link.txt — onde você pode colar o link do seu template Figma

README.md — instruções de uso, como transformar em repo Git e comandos úteis

Próximos passos recomendados

Baixe o ZIP e extraia.

Suba o MongoDB: docker-compose up -d

Instale dependências e rode a API: uvicorn app.main:app --reload

Rode os testes: pytest -v

Suba para um repositório GitHub, se quiser compartilhar/versão.