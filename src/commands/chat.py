import click

@click.command()
@click.option('--model', '-m', default='gpt-3.5-turbo', help='Specify the model to use')
@click.option('--temperature', '-t', type=float, default=0.7, help='Control response randomness (between 0-1)')
def chat(model, temperature):
    """Start Chat Session

    Start an interactive chat session. You can customize model parameters through options.
    """
    try:
        if not get_api_key():
            click.echo("Error: API key not set. Please run 'deepchat config api <your-key>' to set your API key", err=True)
            exit(1)
        
        click.echo(f"Starting chat session... (Model: {model}, Temperature: {temperature})")
        # TODO: Implement actual chat logic
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        exit(1)