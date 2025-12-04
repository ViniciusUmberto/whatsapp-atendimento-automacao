import os
from flask import Flask, request, jsonify

from src.sheets_client import append_event_row

# Inicializa o app Flask
app = Flask(__name__)

# Token de verificação do webhook do WhatsApp
VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "meu_token_secreto")

# Endpoint para verificação do webhook
@app.route("/webhook", methods=["GET"])
def verify_webhook():
    """
    Endpoint usado pelo WhatsApp para verificar o webhook.
    Ele envia hub.mode, hub.verify_token e hub.challenge como query params.
    Se o verify_token bater com o nosso, devemos devolver o hub.challenge.
    """
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    else:
        return "Forbidden", 403

# Endpoint para receber mensagens/eventos do WhatsApp
@app.route("/webhook", methods=["POST"])

def receive_webhook():
    """
    Endpoint que recebe as mensagens/eventos do WhatsApp.
    Aqui vamos, por enquanto, só imprimir o JSON recebido.
    Depois vamos extrair dados e salvar na planilha.
    """
    # Pega o JSON enviado pelo WhatsApp
    data = request.get_json()
    print("Webhook recebido:", data)

    # Por enquanto só responde 200 OK
    return jsonify({"status": "received"}), 200

# Inicia o servidor Flask
if __name__ == "__main__":
    # Porta padrão do Flask é 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
