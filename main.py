from email.message import EmailMessage
import smtplib
import ssl

meu_email = ''
senha = ''
destinatario_email = ''
assunto = "Testando Python"
body = '''
Teste
'''
em = EmailMessage()

em['From'] = meu_email
em['To'] = destinatario_email
em['Subject'] = assunto
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(meu_email, senha)
    smtp.sendmail(meu_email, destinatario_email, em.as_string())
