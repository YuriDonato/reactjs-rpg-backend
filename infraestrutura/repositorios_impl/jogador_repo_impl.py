# backend/app/infraestrutura/repositorios_impl/jogador_repo_impl.py
from app.dominio.repositorios.jogador_repo import JogadorRepositorio
from app.dominio.entidades.jogador import Jogador

# Simulação de banco de dados in-memory
banco_fake = {}

class JogadorRepositorioImpl(JogadorRepositorio):
    def obter_jogador(self, id: int) -> Jogador:
        jogador = banco_fake.get(id)
        if jogador is None:
            raise Exception("Jogador não encontrado")
        return jogador

    def atualizar_jogador(self, jogador: Jogador) -> Jogador:
        banco_fake[jogador.id] = jogador
        return jogador

    def criar_jogador(self, jogador: Jogador) -> Jogador:
        if jogador.id in banco_fake:
            raise Exception("Jogador já existe")
        banco_fake[jogador.id] = jogador
        return jogador
