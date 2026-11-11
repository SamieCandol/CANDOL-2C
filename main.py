from collections import deque


# ==========================================
# 1. BINARY TREE TRAVERSALS (CANDOL)
# ==========================================

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_bfs(root):
    if not root:
        return
    queue = deque([root])
    output = []

    while queue:
        current = queue.popleft()
        output.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print("Tree BFS Traversal:", " -> ".join(output))


def tree_dfs_preorder(node, output=None):
    if output is None:
        output = []
    if node:
        output.append(node.val)
        tree_dfs_preorder(node.left, output)
        tree_dfs_preorder(node.right, output)
    return output


# ==========================================
# 2. GRAPH TRAVERSALS (Adjacency List)
# ==========================================

def graph_bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    output = []

    while queue:
        current = queue.popleft()
        output.append(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("Graph BFS Traversal:", " -> ".join(output))


def graph_dfs(graph, start_node, visited=None, output=None):
    if visited is None:
        visited = set()
    if output is None:
        output = []

    visited.add(start_node)
    output.append(start_node)

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited, output)

    return output


# ==========================================
# MAIN EXECUTION (Mao ni ang mo-trigger sa output)
# ==========================================
if __name__ == "__main__":
    print("=== CC204 DATA STRUCTURES ASSESSMENT ===")

    # --- Binary Tree Setup (CANDOL) ---
    root = TreeNode('C')
    root.left = TreeNode('A')
    root.right = TreeNode('N')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('O')
    root.right.left = TreeNode('L')

    print("\n--- BINARY TREE ---")
    tree_bfs(root)
    dfs_tree_result = tree_dfs_preorder(root)
    print("Tree DFS (Pre-Order) Traversal:", " -> ".join(dfs_tree_result))

    # --- Graph Setup (CANDOL) ---
    graph = {
        'C': ['A', 'N'],
        'A': ['D', 'O'],
        'N': ['L'],
        'D': [],
        'O': [],
        'L': []
    }

    print("\n--- GRAPH ---")
    graph_bfs(graph, 'C')
    dfs_graph_result = graph_dfs(graph, 'C')
    print("Graph DFS Traversal:", " -> ".join(dfs_graph_result))