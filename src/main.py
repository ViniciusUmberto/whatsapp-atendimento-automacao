from src.events import (
    registrar_mensagem_cliente,
    registrar_resposta_equipe,
    registrar_finalizacao,
)


def main():
    numero_cliente = "+5511999999999"
    id_conversa = "conversa-123"

    # Teste 1: registrar mensagem do cliente
    registrar_mensagem_cliente(numero_cliente, id_conversa)

    # Teste 2: registrar resposta da equipe
    registrar_resposta_equipe(numero_cliente, id_conversa)

    # Teste 3: registrar finalização
    registrar_finalizacao(numero_cliente, id_conversa)


if __name__ == "__main__":
    main()
