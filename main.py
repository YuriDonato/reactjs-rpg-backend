from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from interfaces.roteadores import jogador  # Importe outros roteadores conforme forem criados

app = FastAPI(title="RPG Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajuste para os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jogador.router, prefix="/jogador", tags=["Jogador"])
