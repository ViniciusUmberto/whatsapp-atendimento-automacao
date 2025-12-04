from datetime import datetime
from typing import Optional

from src.sheets_client import append_event_row


def _agora_str() -> str:
    """Retorna data e hora atual no formato padrão."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def registrar_mensagem_cliente(numero_cliente: str, id_conversa: str):
    """
    Registra o início do atendimento quando o cliente envia a primeira mensagem.

    Preenche:
    - numero_cliente
    - data_hora_mensagem_cliente (agora)
    - data_hora_resposta_equipe (vazio)
    - data_hora_finalizacao (vazio)
    - id_conversa
    """
    row = [
        numero_cliente,
        _agora_str(),
        "",
        "",
        id_conversa,
    ]
    append_event_row(row)


def registrar_resposta_equipe(numero_cliente: str, id_conversa: str,
                              data_hora_resposta: Optional[str] = None):
    """
    (Versão 1, simplificada)
    Registra a hora da resposta da equipe.

    Nesta primeira versão, vamos só adicionar uma nova linha com o campo de resposta preenchido.
    Depois vamos evoluir para atualizar a linha existente.
    """
    if data_hora_resposta is None:
        data_hora_resposta = _agora_str()

    row = [
        numero_cliente,
        "",
        data_hora_resposta,
        "",
        id_conversa,
    ]
    append_event_row(row)


def registrar_finalizacao(numero_cliente: str, id_conversa: str,
                          data_hora_finalizacao: Optional[str] = None):
    """
    (Versão 1, simplificada)
    Registra a hora em que o atendimento foi finalizado.

    Também começa só adicionando nova linha; depois faremos atualização da mesma linha.
    """
    if data_hora_finalizacao is None:
        data_hora_finalizacao = _agora_str()

    row = [
        numero_cliente,
        "",
        "",
        data_hora_finalizacao,
        id_conversa,
    ]
    append_event_row(row)
