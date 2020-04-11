import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'EmailBOT'
email['to'] = 'farhaan10j@gmail.com'
email['subject'] = 'CAUTION'

email.set_content(html.substitute({'name': 'HUMAN'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('emailgen11@gmail.com', 'qwerty123!@#')
  smtp.send_message(email)
  print('all good !')