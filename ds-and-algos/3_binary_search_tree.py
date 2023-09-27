class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


def inorder(node: Node):
    if not node:
        return
    inorder(node.left)
    print(str(node) + ' -> ', end='')
    inorder(node.right)


def preorder(node: Node):
    if not node:
        return
    print(str(node) + ' -> ', end='')
    preorder(node.left)
    preorder(node.right)


def postorder(node: Node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(str(node) + ' -> ', end='')


def search(node: Node, value: int):
    if not node:
        return None
    if node.value < value:
        return search(node.right, value)
    elif node.value > value:
        return search(node.left, value)
    elif node.value == value:
        return value


def insert(node: Node, value: int):
    if value < node.value and not node.left:
        node.left = Node(value)
        return value
    elif value > node.value and not node.right:
        node.right = Node(value)
        return value
    if value < node.value and node.left:
        return insert(node.left, value)
    elif value > node.value and node.right:
        return insert(node.right, value)


def main():
    node_27 = Node(27)
    node_14 = Node(14)
    node_10 = Node(10)
    node_19 = Node(19)
    node_35 = Node(35)
    node_31 = Node(31)
    node_42 = Node(42)

    node_27.left = node_14
    node_27.right = node_35

    node_14.left = node_10
    node_14.right = node_19

    node_35.left = node_31
    node_35.right = node_42

    search_result = search(node_27, 35)
    print('Result is', search_result)

    insert(node_27, 45)
    print('Inserted', 45)

    preorder(node_27)
    print()

    inorder(node_27)
    print()

    postorder(node_27)
    print()


if __name__ == "__main__":
    main()
