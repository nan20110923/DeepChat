import click
from config.config import get_api_key, set_api_key

@click.group()
def config():
    """Configuration Management

    Manage DeepChat configurations, including API key settings.
    """
    pass

@config.command()
@click.argument('api_key', required=False)
def api(api_key):
    """Manage API Key

    Show current API key when no argument provided, set new API key when argument is provided.
    """
    if api_key:
        try:
            if set_api_key(api_key):
                click.echo("API key set successfully", err=True)
            else:
                click.echo("Error: Unable to set API key", err=True)
                exit(1)
        except Exception as e:
            click.echo(f"Error: {str(e)}", err=True)
            exit(1)
    else:
        try:
            current_key = get_api_key()
            if current_key:
                click.echo(current_key)
            else:
                click.echo("API key not set", err=True)
                exit(1)
        except Exception as e:
            click.echo(f"Error: {str(e)}", err=True)
            exit(1)