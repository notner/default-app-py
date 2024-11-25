import click

@click.command()
def main():
	print('hello')


@click.command('psql', short_help='start up psql-client')
def psql():
	print('psql')
