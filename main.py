from email.message import EmailMessage
import smtplib
import ssl

remetente_email = ''
senha = ''
destinatario_email = ''
assunto = "Testando Python"
body = '''
Teste
'''
email = EmailMessage()

email['From'] = remetente_email
email['To'] = destinatario_email
email['Subject'] = assunto
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(meu_email, senha)
    smtp.sendmail(meu_email, destinatario_email, email.as_string())
