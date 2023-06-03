import click
import uuid
import json
from prettytable import PrettyTable


@click.command('add')
@click.argument('title')
def add_todo(title):
    todo = {'id': str(uuid.uuid4()), 'title': title, 'completed': False}
    data = _load_data()
    data[todo.get('id')] = todo
    _save_data(list(data.values()))
    click.echo(todo)


@click.command('remove')
@click.argument('id')
def remove_todo(id):
    data = _load_data()
    removed_data = data.pop(id, None)
    _save_data(list(data.values()))
    click.echo(removed_data)


@click.command('list')
def list_todo():
    table = PrettyTable(['id', 'title', 'completed'])
    data = list(_load_data().values())
    for x in data:
        table.add_row(list(x.values()))
    click.echo(table)


@click.command('complete')
@click.argument('id')
def complete_todo(id):
    data = _load_data()
    todo = data.get(id)
    todo['completed'] = True
    _save_data(list(data.values()))
    click.echo(todo)


def _load_data():
    data = {}
    try:
        with open('data.json', 'r') as file:
            json_data = json.loads(file.read())
            data = {x.get('id'): x for x in json_data}
    except FileNotFoundError as e:
        pass
    except Exception as e:
        raise e
    return data


def _save_data(data):
    with open('data.json', 'w') as file:
        file.write(json.dumps(data))
