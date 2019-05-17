import glob 
import yaml 
import markdown
from jinja2 import Template
from looker import Looker
from email_client import EmailConfig

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def find_jobs(jobs_file):
	with open(jobs_file, 'r') as stream:
		data = yaml.load(stream, Loader=Loader)

	return data['jobs']

def run_job(jobs_file, template_directory, job_name, base_url, client_id, client_secret, port):
	
	jobs = find_jobs(jobs_file)

	for job in jobs:
		if job['name'] == job_name:
			job_details = job

	if not job:
		raise Exception("Job of that name doesn't exist in file.")

	email_config = EmailConfig()
	email_config.add_config(
			to_email=job_details['to_email'],
			from_email=job_details['from_email'],
			subject=job_details['subject']
		)

	# Connect to client
	client = Looker(base_url, client_id, client_secret, port)

	# Load template
	f = open('{}/{}.md'.format(template_directory, job_details['template']), 'r')
	TEMPLATE = f.read()
	f.close()

	# Add the necessary functions to the Jinja environment
	email_template = Template(TEMPLATE)
	email_template.globals['look_single_value'] = client.get_look_single_value
	email_template.globals['look_table'] = client.get_look_table
	email_template.globals['look_png'] = client.get_look_png

	# Render the Jinja2 template, inserting the relevant values
	extensions = ['extra', 'smarty', 'markdown.extensions.tables']
	doc = email_template.render()

	# Convert the Markdown as HTML5
	html = markdown.markdown(doc, extensions=extensions, output_format='html5')
	email_config.add_content(html)
	email_config.send_email()
