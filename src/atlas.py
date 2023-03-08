import os
import click


class Atlas(object):
    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or '.')
        self.debug = debug


@click.group()
@click.option('--atlas-home', envvar='ATLAS_HOME', default='.atlas')
@click.option('--debug/--nodebug', default=False, envvar='ATLAS_DEBUG')
@click.pass_context
def cli(ctx, atlas_home, debug):
    ctx.obj = Atlas(atlas_home, debug)


pass_atlas = click.make_pass_decorator(Atlas, ensure=True)


@cli.command()
@click.argument('src')
@click.argument('dest', required=False)
@pass_atlas
def clone(repo, src, dest):
    click.echo(src)


@cli.command()
@pass_atlas
def cp(repo):
    click.echo(isinstance(repo, Atlas))


if __name__ == '__main__':
    cli()
