# backend/app/main.py
from fastapi import FastAPI
from app.interfaces.roteadores import jogador, inventario  # Adicione outros roteadores conforme necessário

app = FastAPI(title="RPG Backend")

app.include_router(jogador.router, prefix="/jogador", tags=["Jogador"])
app.include_router(inventario.router, prefix="/inventario", tags=["Inventário"])
# Adicione aqui outros roteadores, por exemplo, quest, equipamento, loja, combate, áreas, auth, etc.
