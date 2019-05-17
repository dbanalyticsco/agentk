import click
import markdown
from jinja2 import Template
from looker import Looker
from email_client import EmailConfig

@click.group()
def cli():
	pass

@click.command()
@click.argument('base_url', envvar='LOOKER_BASE_URL')
@click.argument('client_id', envvar='LOOKER_CLIENT_ID')
@click.argument('client_secret', envvar='LOOKER_CLIENT_SECRET')
@click.option('--port', default=19999)
def run(base_url, client_id, client_secret, port):

	# Connect to client
	client = Looker(base_url, client_id, client_secret, port)

	# Load template
	f = open('example_content/example.md', 'r')
	TEMPLATE = f.read()
	f.close()

	# Add the necessary functions to the Jinja environment
	email_template = Template(TEMPLATE)
	email_template.globals['look_single_value'] = client.get_look_single_value
	email_template.globals['look_table'] = client.get_look_table
	email_template.globals['look_png'] = client.get_look_png

	email_config = EmailConfig()
	email_template.globals['config'] = email_config.add_config

	# Render the Jinja2 template, inserting the relevant values
	extensions = ['extra', 'smarty', 'markdown.extensions.tables']
	doc = email_template.render()

	# Convert the Markdown as HTML5
	html = markdown.markdown(doc, extensions=extensions, output_format='html5')
	email_config.add_content(html)
	email_config.send_email()
	
	# Write to .html file
	f = open("rendered_content/demofile.html", "w")
	f.write(email_config.content)
	f.close()
	

cli.add_command(run)

if __name__ == '__main__':
	cli()