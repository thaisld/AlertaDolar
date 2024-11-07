import requests
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])

import smtplib 
import email.message 

def enviar_email(cotacao): 
    Corpo_email = f"""
    <p>Dólar está abaixo de R$5.70, Cotação atual: R${cotacao}</p> corpo_email
    """
    
    msg = email.Massage()
    msg['Subject'] = "Dólar está hoje abaixo de 5.70"
    msg['From'] = '1134874@atitus.edu.br'
    msg['To'] = '1134874@atitus.edu.br'
    Password = 'zrujbpbxezkksygh'
    msg.add_header('Content-Type','text/html')
    msg.set_payload(Corpo_email)

    s = smtplib.SMTP('smpt.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], Password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print ('Email enviado')

if cotacao < 5.70:
    enviar_email(cotacao)
