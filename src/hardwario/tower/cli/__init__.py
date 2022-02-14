import logging
import click

logger = logging.getLogger(__name__)


@click.group(name='tower', help='Commands for TOWER (Industrial IoT Kit Developer).')
@click.pass_context
def cli(ctx):
    pass
