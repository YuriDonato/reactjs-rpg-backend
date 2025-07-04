from typing import List
from pydantic import BaseModel
from abc import ABC, abstractmethod

from infra.firebase import db  # Certifique-se de que este módulo já esteja configurado com o Firestore


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    in_stock: bool = False


class ItemTemplate(ABC):
    @abstractmethod
    def obter_item(self, id: str) -> dict:
        pass

    @abstractmethod
    def atualizar_item(self, id: str, item: Item) -> dict:
        pass

    @abstractmethod
    def criar_item(self, item: Item) -> dict:
        pass

    @abstractmethod
    def deletar_item(self, id: str) -> None:
        pass

    @abstractmethod
    def listar_itens(self) -> List[dict]:
        pass

    @abstractmethod
    def listar_itens_disponiveis(self) -> List[dict]:
        pass

    @abstractmethod
    def listar_itens_por_preco(self) -> List[dict]:
        pass


class ItemFirebase(ItemTemplate):
    def criar_item(self, item: Item) -> dict:
        doc_ref = db.collection("items").document()
        doc_ref.set(item.dict())
        return {"id": doc_ref.id, **item.dict()}

    def obter_item(self, id: str) -> dict:
        doc_ref = db.collection("items").document(id)
        doc = doc_ref.get()
        if not doc.exists:
            raise Exception("Item não encontrado")
        return {"id": doc.id, **doc.to_dict()}

    def atualizar_item(self, id: str, item: Item) -> dict:
        doc_ref = db.collection("items").document(id)
        if not doc_ref.get().exists:
            raise Exception("Item não encontrado")
        doc_ref.update(item.dict())
        return {"id": id, **item.dict()}

    def deletar_item(self, id: str) -> None:
        doc_ref = db.collection("items").document(id)
        if not doc_ref.get().exists:
            raise Exception("Item não encontrado")
        doc_ref.delete()

    def listar_itens(self) -> List[dict]:
        docs = db.collection("items").stream()
        itens = []
        for doc in docs:
            dados = doc.to_dict()
            dados["id"] = doc.id
            itens.append(dados)
        return itens

    def listar_itens_disponiveis(self) -> List[dict]:
        docs = db.collection("items").where("in_stock", "==", True).stream()
        itens = []
        for doc in docs:
            dados = doc.to_dict()
            dados["id"] = doc.id
            itens.append(dados)
        return itens

    def listar_itens_por_preco(self) -> List[dict]:
        docs = db.collection("items").order_by("price").stream()
        itens = []
        for doc in docs:
            dados = doc.to_dict()
            dados["id"] = doc.id
            itens.append(dados)
        return itens
