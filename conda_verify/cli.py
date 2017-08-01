import os

import click

from conda_verify.verify import Verify
from conda_verify.utilities import render_metadata, iter_cfgs


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--ignore', nargs=1, type=str)
@click.option('--exit', is_flag=True)
@click.version_option(prog_name='conda-verify')
def cli(path, ignore, exit):
    """"""
    verifier = Verify()
    if ignore:
        ignore = ignore.split(',')

    meta_file = os.path.join(path, 'meta.yaml')
    if os.path.isfile(meta_file):
        print('Verifying {}...' .format(meta_file))
        for cfg in iter_cfgs():
            meta = render_metadata(path, cfg)
            verifier.verify_recipe(rendered_meta=meta, recipe_dir=path,
                                   checks_to_ignore=ignore, exit_on_error=exit)

    elif path.endswith(('.tar.bz2', '.tar')):
        print('Verifying {}...' .format(path))
        verifier.verify_package(path_to_package=path, checks_to_ignore=ignore,
                                exit_on_error=exit)
