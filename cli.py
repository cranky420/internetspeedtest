import click
from rich import print
from speed import test_speed

@click.command()
def cli():

    print(
        "[cyan]Running internet test...[/cyan]"
    )

    result = test_speed()

    print()

    print(
        f"[green]Download:[/green] {result['download']} Mbps"
    )

    print(
        f"[green]Upload:[/green] {result['upload']} Mbps"
    )

    print(
        f"[green]IP:[/green] {result['ip']}"
    )

if __name__ == "__main__":
    cli()