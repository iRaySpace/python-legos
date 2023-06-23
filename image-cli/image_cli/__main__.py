import click
from .command import convert


@click.group()
def main():
    pass

main.add_command(convert)


if __name__ == '__main__':
    main()
