# backend/app/interfaces/roteadores/inventario.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

# Simulação de banco de dados para inventário (in-memory)
inventario_db = {"itens": []}

class InventarioDTO(BaseModel):
    itens: List[Dict]

@router.get("/", response_model=InventarioDTO)
def obter_inventario():
    return inventario_db

@router.put("/", response_model=InventarioDTO)
def atualizar_inventario(inventario: InventarioDTO):
    inventario_db["itens"] = inventario.itens
    return inventario_db
