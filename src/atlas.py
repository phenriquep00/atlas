import click

@click.command()
def hello():
    click.echo("testing")

if __name__ == '__main__':
    hello()