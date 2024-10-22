import click
from pathlib import Path
import typing
from ..utils.printer import print_result

if typing.TYPE_CHECKING:
    from ..client import Primitive


@click.command("lint")
@click.pass_context
@click.argument("source", type=click.Path(exists=True), default=".")
def cli(context, source: str):
    """Lint"""
    primitive: Primitive = context.obj.get("PRIMITIVE")
    result, message = primitive.lint.execute(source=Path(source))
    print_result(message=message, context=context)
