from setuptools import setup, find_packages

with open("README.md", "r") as fs:
    long_description = fs.read()

setup(
    name="{{cookiecutter.project_name}}",
    version="0.0.1",
    description="{{cookiecutter.project_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click", "netzeus-cli>=0.0.1"],
    entry_points="""
        [netzeus_cli.plugins]
        {{cookiecutter.entrypoint_command}}={{cookiecutter.project_name}}.core:{{cookiecutter.entrypoint_command_group}}
    """,
    include_package_data=True,
)
