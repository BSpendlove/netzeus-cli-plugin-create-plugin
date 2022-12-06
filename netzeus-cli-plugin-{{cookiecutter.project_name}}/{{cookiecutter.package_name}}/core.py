import click


@click.group("{{cookiecutter.cli_name}}")
def cli() -> None:
    """{{cookiecutter.project_description}}"""
