from dominio.repos.jogador import JogadorRepositorio
from dominio.entidades.jogador import Jogador
from infra.firebase import db

class JogadorRepositorioFirebase(JogadorRepositorio):
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
