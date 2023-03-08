import os
import click


@click.group()
@click.option('--atlas-home', envvar='ATLAS_HOME', default='.atlas')
@click.option('--debug/--nodebug', default=False, envvar='ATLAS_DEBUG')
@click.pass_context
def cli(ctx, atlas_home, debug):
    pass


@cli.command()
@click.argument('src')
@click.argument('dest', required=False)
def atlas(src, dest):
    click.echo(src)


if __name__ == '__main__':
    cli()
