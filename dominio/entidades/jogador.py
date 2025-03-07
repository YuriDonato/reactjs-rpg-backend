from pydantic import BaseModel
from typing import List, Dict

class Jogador(BaseModel):
    id: str
    nome: str
    hp: int
    xp: int
    nivel: int
    ouro: int
    inventario: List[Dict] = []
    quests: List[Dict] = []
    equipamentos: Dict = {}

    class Config:
        from_attributes = True
