import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class EmailConfig:

	def __init__(self):

		self.to_email = None
		self.from_email = None
		self.subject = None
		self.content = None

	def add_config(self, to_email, from_email, subject):

		self.to_email = to_email
		self.from_email = from_email
		self.subject = subject

		return ''

	def add_content(self, html_content):

		self.content = html_content

	def send_email(self):

		message = Mail(
		    from_email=self.from_email,
		    to_emails=self.to_email,
		    subject=self.subject,
		    html_content=self.content)
		try:
		    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
		    response = sg.send(message)
		except Exception as e:
		    print(e.message)

