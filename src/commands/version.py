import click

@click.command()
def version():
    """Show version information"""
    click.echo("DeepChat v0.1.0")