import click
from runner import run_job, find_jobs

@click.group()
def cli():
	pass

@click.command()
@click.argument('jobs_file')
def jobs(jobs_file):
	
	print(find_jobs(jobs_file))

@click.command()
@click.argument('jobs_file')
@click.argument('template_directory')
@click.argument('job_name')
@click.argument('base_url', envvar='LOOKER_BASE_URL')
@click.argument('client_id', envvar='LOOKER_CLIENT_ID')
@click.argument('client_secret', envvar='LOOKER_CLIENT_SECRET')
@click.option('--port', default=19999)
def run(jobs_file, template_directory, job_name, base_url, client_id, client_secret, port):
	
	run_job(jobs_file, template_directory, job_name, base_url, client_id, client_secret, port)

cli.add_command(run)
cli.add_command(jobs)

if __name__ == '__main__':
	cli()