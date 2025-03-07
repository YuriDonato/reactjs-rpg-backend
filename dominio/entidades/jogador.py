# backend/app/dominio/entidades/jogador.py
from pydantic import BaseModel
from typing import List, Dict

class Jogador(BaseModel):
    id: int
    nome: str
    hp: int
    xp: int
    nivel: int
    ouro: int
    inventario: List[Dict] = []
    quests: List[Dict] = []
    equipamentos: Dict = {}

    class Config:
        orm_mode = True
