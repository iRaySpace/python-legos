Todo CLI

Installation
```
poetry install
```

Usage
```bash
python -m todo_cli add "Buy groceries"
# {'id': '8cc11f36-f467-4880-b520-818a2ff2ef58', 'title': 'Buy groceries', 'completed': False}

python -m todo_cli add "Buy toys"
# {'id': '17364876-a04d-474f-b125-a12dd137f069', 'title': 'Buy toys', 'completed': False}

python -m todo_cli remove "17364876-a04d-474f-b125-a12dd137f069"
# {'id': '17364876-a04d-474f-b125-a12dd137f069', 'title': 'Buy toys', 'completed': False}

python -m todo_cli complete "8cc11f36-f467-4880-b520-818a2ff2ef58"
# {'id': '8cc11f36-f467-4880-b520-818a2ff2ef58', 'title': 'Buy groceries', 'completed': True}

python -m todo_cli list
# +--------------------------------------+---------------+-----------+
# |                  id                  |     title     | completed |
# +--------------------------------------+---------------+-----------+
# | 8cc11f36-f467-4880-b520-818a2ff2ef58 | Buy groceries |    True   |
# +--------------------------------------+---------------+-----------+
```
