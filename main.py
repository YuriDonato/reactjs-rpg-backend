from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from roteadores import inicial, jogador, item

app = FastAPI(title="RPG Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajuste para os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Inicial"], response_model=dict)
async def pagina_inicial():
    return {"message": "Olá"}


app.include_router(jogador.router, prefix="/jogador", tags=["Jogador"])
app.include_router(item.router, prefix="/item", tags=["Item"])
