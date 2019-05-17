import click
import markdown
from jinja2 import Template

TEMPLATE="""
Hello, 

## This is an email from Dylan. 

{% if new_clients_count < 0 %}
We lost {{ new_clients_count|abs }} clients yesterday.
{% else %}
We added {{ new_clients_count }} new clients yesterday.
{% endif %}
"""

@click.group()
def cli():
	pass

@click.command()
@click.argument('new_clients_count')
def run(new_clients_count):
	extensions = ['extra', 'smarty']
	doc = Template(TEMPLATE).render(new_clients_count=int(new_clients_count))
	html = markdown.markdown(doc, extensions=extensions, output_format='html5')
	print(html)
	

cli.add_command(run)

if __name__ == '__main__':
	cli()