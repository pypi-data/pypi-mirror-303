import click
from pygutz.commands.template import HexTemplate

@click.group()
def command_executor():
    pass

@click.command()
@click.option("--project-name", help="Set project name", type=str)
def createproject(name: str):
    if name is None:
        exec = HexTemplate()
        exec.generate()
    else:
        exec = HexTemplate(name)
        exec.generate()

command_executor.add_command(createproject)