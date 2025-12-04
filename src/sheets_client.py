import os
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build



#permissao para acessar e editar a planilha
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#caminho dos arquivos de credenciais e token
CREDENTIALS_FILE = Path("credentials.json")

#caminho do token de acesso
TOKEN_FILE = Path("token.json")

#ID da planilha e intervalo de dados  
SPREADSHEET_ID = "1NweLXdiyufYnXFddzYX6OX34IOiQsXr4_A8ptXvLsBo"
RANGE = "Eventos!A2:E"

def get_sheets_service():
    creds = None
    #verifica se o token ja existe
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # se nao existir, faz o fluxo de autorizacao
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # atualiza o token
            creds.refresh(Request())
        else:
            # se nao, faz o login
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # salva o token para futuras execucoes
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    service = build('sheets', 'v4', credentials=creds)
    return service

def append_event_row(row_values: list):
    """
    Adiciona uma nova linha na planilha de eventos.
    row_values deve ser uma lista com 5 elementos:
    [numero_cliente, data_hora_msg, data_hora_resposta, data_hora_finalizacao, id_conversa]
    """
    service = get_sheets_service()

    body = {
        "values": [row_values]
    }

    result = (
        service.spreadsheets()
        .values()
        .append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE,
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body=body,
        )
        .execute()
    )

    return result