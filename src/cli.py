import click
from commands.chat import chat
from commands.version import version
from commands.config import config

@click.group()
def cli():
    """DeepChat CLI
    
    A powerful AI chat tool that supports multiple models and configuration options.
    Use 'deepchat <command> --help' to view help information for specific commands.
    """
    pass

cli.add_command(chat)
cli.add_command(version)
cli.add_command(config)

if __name__ == "__main__":
    cli()