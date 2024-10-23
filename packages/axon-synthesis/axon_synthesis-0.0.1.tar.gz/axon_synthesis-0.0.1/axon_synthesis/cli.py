"""Command Line Interface for the axon_synthesis package."""

import click

import axon_synthesis.example


@click.command("axon-synthesis")
@click.version_option()
@click.option(
    "-x",
    "--x_value",
    required=True,
    type=int,
    help="The value of X.",
)
@click.option(
    "-y",
    "--y_value",
    required=True,
    type=int,
    help="The value of Y.",
)
def main(x_value, y_value):
    """Add the values of X and Y."""
    print(f"{x_value} + {y_value} = {axon_synthesis.example.add(x_value, y_value)}")
