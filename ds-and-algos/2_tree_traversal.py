class Node:
    def __init__(self, item: int):
        self.left = None
        self.right = None
        self.item = item


def inorder(root_node: Node):
    if not root_node:
        return
    inorder(root_node.left)
    print(str(root_node.item) + ' -> ', end='')
    inorder(root_node.right)


def preorder(root_node: Node):
    if not root_node:
        return
    print(str(root_node.item) + ' -> ', end='')
    preorder(root_node.left)
    preorder(root_node.right)


def postorder(root_node: Node):
    if not root_node:
        return
    postorder(root_node.left)
    postorder(root_node.right)
    print(str(root_node.item) + ' -> ', end='')


def main():
    root_node = Node(1)
    twelve_node = Node(12)
    nine_node = Node(9)
    five_node = Node(5)
    six_node = Node(6)

    root_node.left = twelve_node
    root_node.right = nine_node

    twelve_node.left = five_node
    twelve_node.right = six_node

    inorder(root_node)
    print()

    preorder(root_node)
    print()

    postorder(root_node)
    print()


if __name__ == "__main__":
    main()
