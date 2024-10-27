import time


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value 

    def __str__(self):
        return str(self.value)


def _reverse(stack):
    result = []
    while stack:
        popped = stack.pop()
        result.append(popped)
    return result


def _preorder(root):
    stack = [root]
    result = []

    while stack:
        popped = stack.pop()
        if popped.right: stack.append(popped.right)
        if popped.left: stack.append(popped.left)        
        result.append(popped.value)

    return result


# def _postorder(root):
#     stack = [root]
#     result = []

#     while stack:
#         popped = stack.pop()
#         if popped.left: stack.append(popped.left)
#         if popped.right: stack.append(popped.right)
#         result.append(popped.value)

#     return _reverse(result)


def _postorder(root):
    result = []
    stack = []
    current = root
    last_visited = None
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            backtracked = stack[-1]
            if backtracked.right and last_visited != backtracked.right:
                current = backtracked.right
            else:
                result.append(backtracked.value)
                last_visited = stack.pop()

    return result


def _inorder(root):
    result = []
    stack = []
    current = root
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            last_visited = stack.pop()
            if last_visited.right:
                current = last_visited.right
            result.append(last_visited.value)

    return result


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    print("Preorder:", _preorder(root))
    print("Postorder:", _postorder(root))
    print("Inorder:", _inorder(root))


if __name__ == "__main__":
    main()
