import typer

from labctl import __version__

app = typer.Typer()

@app.callback()
def callback():
    """
    labctl
    """


@app.command()
def version():
    """
    Print the version
    """
    typer.echo("labctl version {}".format(__version__))
