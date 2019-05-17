import click
import markdown
from jinja2 import Template

TEMPLATE="""
Hello, 

## This is an email from Dylan. 

{% if new_clients_count < 0 %}
We lost {{ multiply_by_two(new_clients_count)|abs }} clients yesterday.
{% else %}
We added {{ multiply_by_two(new_clients_count) }} new clients yesterday.
{% endif %}
"""

@click.group()
def cli():
	pass

def multiply_by_two(number):
	return number*2

@click.command()
@click.argument('new_clients_count')
def run(new_clients_count):

	# Add the necessary functions to the Jinja environment
	template = Template(TEMPLATE)
	template.globals['multiply_by_two'] = multiply_by_two

	# Render the Jinja2 template, inserting the relevant values
	extensions = ['extra', 'smarty']
	doc = Template(TEMPLATE).render(new_clients_count=int(new_clients_count))

	# Convert the Markdown as HTML5
	html = markdown.markdown(doc, extensions=extensions, output_format='html5')
	print(html)
	

cli.add_command(run)

if __name__ == '__main__':
	cli()