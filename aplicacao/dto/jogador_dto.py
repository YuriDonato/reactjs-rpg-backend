# backend/app/aplicacao/dto/jogador_dto.py
from pydantic import BaseModel
from typing import List, Dict

class JogadorDTO(BaseModel):
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
