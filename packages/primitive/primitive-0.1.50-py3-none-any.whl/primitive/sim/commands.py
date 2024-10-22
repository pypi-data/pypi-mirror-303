import click
from pathlib import Path
import typing
from typing import Tuple
from ..utils.printer import print_result

if typing.TYPE_CHECKING:
    from ..client import Primitive


@click.command("sim")
@click.pass_context
@click.argument("cmd", nargs=-1, required=True)
@click.option("--source", type=click.Path(exists=True), default=".")
def cli(context, source: str, cmd: Tuple[str]) -> None:
    """Sim"""
    primitive: Primitive = context.obj.get("PRIMITIVE")
    result, message = primitive.sim.execute(source=Path(source), cmd=cmd)
    print_result(message=message, context=context)
