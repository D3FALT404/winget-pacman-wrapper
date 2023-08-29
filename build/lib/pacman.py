import click
import os

@click.command()
@click.option("-S", "--install", type=str, default="")
def cli(install):
    if install:
        apps = install.split(" ")
        for app in apps:
            os.system(f"winget install {app} -s winget")

    """Simple program that greets NAME for a total of COUNT times."""

if __name__ == '__main__':
    cli()
