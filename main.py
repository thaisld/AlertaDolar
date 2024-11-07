import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime
import os

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])

def registrar_cotacao(cotacao):
    diretorio = "data"
    os.makedirs(diretorio, exist_ok=True)
    caminho_arquivo = os.path.join(diretorio, "cotacoes.txt")
    
    with open(caminho_arquivo, "a", encoding="utf-8") as file:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{agora} - Cotação: R${cotacao}\n")

def enviar_email(cotacao):
    Corpo_email = f"""
    <p>Dólar está abaixo de R$5.70, Cotação atual: R${cotacao}</p>
    """
    
    msg = EmailMessage()
    msg['Subject'] = "Dólar está hoje abaixo de 5.70"
    msg['From'] = '1134874@atitus.edu.br'
    msg['To'] = '1134874@atitus.edu.br'
    Password = 'zrujbpbxezkksygh'
    msg.set_content(Corpo_email, subtype='html')

    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(msg['From'], Password)
        s.send_message(msg)
        print('Email enviado')

if cotacao < 5.70:
    enviar_email(cotacao)

registrar_cotacao(cotacao)
