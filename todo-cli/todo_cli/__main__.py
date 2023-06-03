import click
from .command import add_todo, remove_todo, list_todo, complete_todo


@click.group()
def main():
    pass

main.add_command(add_todo)
main.add_command(remove_todo)
main.add_command(list_todo)
main.add_command(complete_todo)


if __name__ == '__main__':
    main()
