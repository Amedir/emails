import smtplib
import email.message
from dotenv import load_dotenv
import os

class Gmail:

    def __init__(self, emailSubject, emailFrom, emailTo, password, emailBody):
        self.emailSubject = emailSubject
        self.emailFrom = emailFrom
        self.emailTo = emailTo
        self.password = password
        self.emailBody = emailBody

    def __repr__(self):
        return f"O email com assunto '{self.emailSubject}', está criado"

    def enviar_email(self):
        msg = email.message.Message()
        msg['Subject'] = self.emailSubject
        msg['From'] = self.emailFrom
        msg['To'] = self.emailTo
        toListEmails = self.emailTo.split(',')
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(self.emailBody)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], self.password)
        s.sendmail(from_addr=msg['From'], to_addrs=toListEmails, msg=msg.as_string().encode('utf-8'))
        print('Email enviado')

if __name__ == '__main__':

    corpo_email = """
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    """

    # Carrega as variaveis do arquivo .env
    load_dotenv()
    SENHA = os.getenv('SENHA') # Senha do seu email
    FROM = os.getenv('FROM') # Seu email para acesso e envio do email como remetente
    TO = os.getenv('TO') # Para quem o email será enviado

    emailObject = Gmail(emailFrom=FROM, password=SENHA, emailBody=corpo_email, 
                        emailSubject='Aqui vai o assunto do email', emailTo=TO)
    
    emailObject.enviar_email()