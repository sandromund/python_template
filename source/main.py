"""
This module provides functionality to read and validate a YAML configuration file,
and then print a message from the 'demo' section of the configuration. It uses
Pydantic for validation and Click for the command-line interface.

Classes:
    DemoConfig: Represents the 'demo' section of the configuration.
    Config: Represents the entire configuration file structure.
    ConfigFilePath: Represents the configuration file path.

Functions:
    main(config_file_path): Reads and validates the configuration file and prints a message.
    cli(): A Click group to hold CLI commands.
    run(config): A Click command to run the main function with the provided configuration file path.
"""

import click
import yaml
from pydantic import BaseModel, FilePath, ValidationError


class DemoConfig(BaseModel):
    """
    Represents the 'demo' section of the configuration.
    """

    message: str


class Config(BaseModel):
    """
    Represents the entire configuration file structure.
    """

    demo: DemoConfig


class ConfigFilePath(BaseModel):
    """
    Represents the configuration file path.
    """

    path: FilePath


def main(config_file_path: str):
    """
    Reads and validates a YAML configuration file, then prints a message from the 'demo' section.

    Args:
        config_file_path (str): The path to the configuration YAML file.

    Raises:
        ValidationError: If the file path or the YAML content is invalid.
    """
    try:
        # Validate the file path
        file_path = ConfigFilePath(path=config_file_path).path

        # Read and parse the YAML file
        with open(file_path, "r", encoding="utf8") as yaml_file:
            config_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)

        # Validate the YAML content
        config = Config(**config_dict)

        print(config.demo.message)

    except ValidationError as e:
        print("Error in configuration or file path:")
        print(e)


@click.group()
def cli():
    """
    A Click group to hold CLI commands.
    """


@click.command()
@click.option("--config", help="Path to the config file.")
def run(config):
    """
    A Click command to run the main function with the provided configuration file path.

    Args:
        config (str): The path to the configuration file.
    """
    main(config_file_path=config)


cli.add_command(run)

if __name__ == "__main__":
    cli()
