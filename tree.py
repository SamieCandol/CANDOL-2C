class Node:

    def __init__(self, data: str):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(root: Node) -> None:
    if root is not None:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def inorder_traversal(root: Node) -> None:
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


def postorder_traversal(root: Node) -> None:
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")


def main() -> None:
    root = Node('J')
    root.left = Node('E')
    root.right = Node('S')
    root.left.left = Node('S')
    root.left.right = Node('A')

    print("=" * 48)
    print("      DATA STRUCTURES & ALGORITHMS: DFS     ")
    print("=" * 48)
    print("Binary Tree Nodes: J, E, S, S, A\n")

    print("PREORDER  (Root -> Left -> Right) : ", end="")
    preorder_traversal(root)
    print()

    print("INORDER   (Left -> Root -> Right) : ", end="")
    inorder_traversal(root)
    print()

    print("POSTORDER (Left -> Right -> Root) : ", end="")
    postorder_traversal(root)
    print("\n" + "=" * 48)


if __name__ == "__main__":
    main()