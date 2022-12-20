import click

import generate


@click.command()
@click.option("--config", help="Name of configuration file")
@click.option("--output", default=".", help="Output directory")
def cli(config, output):
    """Generate C++ code based on config file"""
    generate.run(config, output)


if __name__ == "__main__":
    cli()
