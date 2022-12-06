# netzeus-cli-plugin-create-plugin

This is a simple Cookiecutter template you can use to generate the project structure for a NetZeus CLI Plugin. You can begin developing your plugin after running the following commands:

```
pip install cookiecutter
cookiecutter https://github.com/BSpendlove/netzeus-cli-plugin-create-plugin
```

The following options will appear to customize your NetZeus CLI Plugin:
```
project_name [NetZeusCLIPlugin]: my-cool-plugin
package_name [netzeus_cli_plugin_my_cool_plugin]: 
cli_name [my-cool-plugin]: 
project_description [NetZeus CLI Plugin automatically generated via cookiecutter]: 
Select python_version:
1 - 3.8
2 - 3.9
3 - 3.10
Choose from 1, 2, 3 [1]: 2
Select virtualenv:
1 - virtualenv
2 - python3
Choose from 1, 2 [1]: 1
author_name [your_name]: Brandon Spendlove
author_email [your_email@example.com]: brandon.spendlove@netzeus.io
```

You can then proceed to install your project in "editable" mode using:
```
pip install -e <project_name>

eg.

pip install -e netzeus-cli-plugin-my-cool-plugin
```

and now you have access to run your first plugin command:
```
netzeus-cli my-cool-plugin --help
Usage: netzeus-cli my-cool-plugin [OPTIONS] COMMAND [ARGS]...

  NetZeus CLI Plugin automatically generated via cookiecutter

Options:
  --help  Show this message and exit.
```

For further developement, please visit the [plugins guide](https://github.com/BSpendlove/netzeus-cli#developing-a-netzeus-cli-plugin) on the NetZeusCLI repository.