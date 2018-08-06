#!/usr/bin/env python

import logging
import click

from .converter import ProtoFaustConverter

logger = logging.getLogger(__name__)


@click.group()
@click.option('-v', '--verbose', is_flag=True)
@click.pass_context
def cli(ctx, verbose):
    if verbose:
        logger.info('Running ProtoFaust in verbose mode')
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    ctx.obj = ProtoFaustConverter()


@cli.command(help="Build and generate Faust records from Protobuf files in directory")
@click.argument('input_dir')
@click.argument('output_dir')
@click.option('--validate', 'validate', flag_value=True, default=False)
@click.pass_context
def convert(ctx, input_dir, output_dir, validate):
    try:
        pfc = ProtoFaustConverter(input_dir=input_dir, output_dir=output_dir, validate=validate)
        pfc.run()
    except Exception as e:
        logger.exception('Unhandled Exception')
        ctx.exit(-1)


def main():
    cli()


if __name__ == "__main__":
    main()
