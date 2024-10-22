import click
from ..utils.printer import print_result
from pathlib import Path
import typing

if typing.TYPE_CHECKING:
    from ..client import Primitive


@click.group("files")
@click.pass_context
def cli(context):
    """Files"""
    pass


@cli.command("upload")
@click.pass_context
@click.argument("path", type=click.Path(exists=True))
@click.option("--public", "-p", help="Is this a Public file", is_flag=True)
@click.option("--key-prefix", "-k", help="Key Prefix", default="")
def file_upload_command(context, path, public, key_prefix):
    """File Upload"""
    primitive: Primitive = context.obj.get("PRIMITIVE")
    path = Path(path)
    result = primitive.files.file_upload(path, is_public=public, key_prefix=key_prefix)
    message = result.json()
    print_result(message=message, context=context)
