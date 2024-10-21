"""Console script for dyutools."""

import click
from .fcov_merge import fcov_merge


@click.group()
def main():
    """Main entrypoint."""
    click.echo("dyutools")
    click.echo("=" * len("dyutools"))
    click.echo("Set of scripts for ASIC Design")


main.add_command(fcov_merge)

if __name__ == "__main__":
    main()  # pragma: no cover
