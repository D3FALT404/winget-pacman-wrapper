import click
import os

@click.command()
@click.option("-S", "--install", type=str, default="")
@click.option("-Ss", "--search", type=str, default="")
@click.option("-Syu", "--update", is_flag=True)
@click.option("-R", "--remove", type=str, default="")
def cli(install, update, search, remove):
    if install:
        click.echo(install)
        apps = string_to_array(install)
        click.echo(apps)
        for app in apps:
            os.system(f'winget install "{app}" -s winget --accept-source-agreements')
    elif remove:
        apps = string_to_array(remove)
        for app in apps:
            os.system(f'winget rm "{app}"')
    elif search:
        os.system(f'winget search "{search}"')
    else:
        os.system("winget update --all")


    """Simple program that greets NAME for a total of COUNT times."""


def string_to_array(string):
    apps = string.split(" ")
    for x in range(len(apps)):
        if '-' in apps[x]:
            apps[x] = apps[x].replace('-', ' ')
    return apps
if __name__ == '__main__':
    cli()
