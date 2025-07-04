from abc import ABC, abstractmethod
from infra.firebase import db
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


class JogadorTemplate(ABC):
    @abstractmethod
    def obter_jogador(self, id: str) -> Jogador:
        pass

    @abstractmethod
    def atualizar_jogador(self, jogador: Jogador) -> Jogador:
        pass

    @abstractmethod
    def criar_jogador(self, jogador: Jogador) -> Jogador:
        pass


class JogadorFirebase(JogadorTemplate):
    collection_name = "jogadores"

    def obter_jogador(self, id: str) -> Jogador:
        doc_ref = db.collection(self.collection_name).document(id)
        doc = doc_ref.get()
        if not doc.exists:
            raise Exception("Jogador não encontrado")
        data = doc.to_dict()
        return Jogador(**data)

    def atualizar_jogador(self, jogador: Jogador) -> Jogador:
        doc_ref = db.collection(self.collection_name).document(jogador.id)
        doc_ref.set(jogador.dict())
        return jogador

    def criar_jogador(self, jogador: Jogador) -> Jogador:
        doc_ref = db.collection(self.collection_name).document(jogador.id)
        if doc_ref.get().exists:
            raise Exception("Jogador já existe")
        doc_ref.set(jogador.dict())
        return jogador
