#!/usr/bin/env python

import logging
import os
import shutil
import click
import sys

from .converter import ProtoFaustConverter

logger = logging.getLogger(__name__)


@click.group()
@click.option('-v', '--verbose', is_flag=True)
@click.pass_context
def cli(ctx, verbose):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    ctx.obj = ProtoFaustConverter()


@cli.command(help="Build and generate Faust records from Protobuf files in directory")
@click.argument('directory')
@click.option('--validate', 'validate', flag_value=True, default=False)
@click.pass_context
def convert(ctx, directory, validate):
    try:
        pfc = ProtoFaustConverter(directory=directory, validate=validate)
        pfc.build()
        pfc.convert()
    except Exception as e:
        logger.exception('Unhandled Exception')
        ctx.exit(-1)


def main():
    cli()


if __name__ == "__main__":
    main()