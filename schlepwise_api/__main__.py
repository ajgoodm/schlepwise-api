import click

from schlepwise_api.app import app


@click.group()
def cli():
    pass


@click.command()
@click.option('--port', type=int, default=4000)
def runserver(port):
    """
    Run the server (development mode) and listen on a port (default 4000)
    """
    app.run(host="0.0.0.0", debug=True, port=port)


cli.add_command(runserver)

try:
    cli()
except Exception:
    app.logger.exception('Failed to execute cli!')