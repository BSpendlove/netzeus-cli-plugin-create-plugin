import click

@click.group("{{cookiecutter.entrypoint_command}}")
def {{cookiecutter.entrypoint_command_group}}() -> None:
    """{{cookiecutter.project_description}}"""
