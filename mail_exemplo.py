import smtplib
from email.mime.text import MIMEText

# Configurações do servidor SMTP (ajuste de acordo com sua configuração)
smtp_server = "seu_servidor_smtp"
smtp_port = 25  # Porta padrão para SMTP
sender_email = "jhonatan@empresa.com.br"
sender_password = "sua_senha"

# Destinatários
receivers = ["aleario1@empresa.com.br", "aleario2@empresa.com.br"]

# Corpo do e-mail
message = MIMEText("Este é um teste de envio de e-mail via SMTP interno.")

# Criação da mensagem
message["From"] = sender_email
message["To"] = ", ".join(receivers)
message["Subject"] = "Assunto do E-mail"

# Conexão com o servidor SMTP
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()  # Identifica o cliente SMTP ao servidor
    # server.starttls()  # Se o servidor exigir TLS, descomente esta linha
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, receivers, text)