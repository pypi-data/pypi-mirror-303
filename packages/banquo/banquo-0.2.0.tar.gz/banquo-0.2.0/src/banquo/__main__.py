"""Command-line interface."""
import click


@click.group()
@click.version_option()
def main() -> None:
    """Banquo."""

@main.command()
def hello() -> None:
    click.echo(f"Hello")


if __name__ == "__main__":
    main(prog_name="banquo")  # pragma: no cover
