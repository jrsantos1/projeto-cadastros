import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ... (configurações do SMTP como no exemplo anterior)

# Corpo do e-mail com tabela HTML
html = """\
<html>
<body>
<p>Este é um e-mail com uma tabela HTML.</p>
<table>
  <tr>
    <th>Coluna 1</th>
    <th>Coluna 2</th>
  </tr>
  <tr>
    <td>Célula 1</td>
    <td>Célula 2</td>
  </tr>
</table>
</body>
</html>
"""

# Criação da mensagem
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receivers)
message["Subject"] = "Assunto do E-mail com Tabela"

# Adiciona o corpo HTML à mensagem
message.attach(MIMEText(html, "html"))

# Conexão com o servidor SMTP e envio do e-mail
# ... (como no exemplo anterior)