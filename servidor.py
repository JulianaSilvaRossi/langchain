from app import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
    title="Meu app de IA",
    description="Traduza seu texto para qualquer idioma",
    version="1.0.0",
)

add_routes(app, chain, path="/translate")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)