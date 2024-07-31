import click
import yaml
from icecream import ic


def main(config_file_path):
    with open(config_file_path, "r", encoding="utf8") as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)
    ic(config["demo"]["message"])


@click.group()
def cli():
    pass


@click.command()
@click.option("--config", help="Path to the config file.")
def run(config):
    main(config_file_path=config)


cli.add_command(run)

if __name__ == "__main__":
    cli()
