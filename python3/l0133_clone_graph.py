class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned = Node(node.val, [])
        queue = [node]
        visited_map = { node: cloned }
        while queue:
            old_node = queue.pop(0)
            new_node = visited_map[old_node]
            for neighbor in old_node.neighbors:
                if neighbor not in visited_map:
                    new_neighbor = Node(neighbor.val, [])
                    new_node.neighbors.append(new_neighbor)
                    visited_map[neighbor] = new_neighbor
                    queue.append(neighbor)
                else:
                    new_node.neighbors.append(visited_map[neighbor])

        return cloned

    def cloneGraphDFSIterative(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned = Node(node.val, [])
        stack = [node]
        visited_map = { node: cloned }
        while stack:
            old_node = stack.pop()
            new_node = visited_map[old_node]
            for neighbor in old_node.neighbors:
                if neighbor not in visited_map:
                    new_neighbor = Node(neighbor.val, [])
                    new_node.neighbors.append(new_neighbor)
                    visited_map[neighbor] = new_neighbor
                    stack.append(neighbor)
                else:
                    new_node.neighbors.append(visited_map[neighbor])

        return cloned

    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        def clonegraph(node, node_map):
            if node in node_map:
                return None
            n = Node(node.val, [])
            node_map[node] = n
            for neighbor in node.neighbors:
                if neighbor in node_map:
                    n.neighbors.append(node_map[neighbor])
                else:
                    nc = clonegraph(neighbor, node_map)
                    n.neighbors.append(nc)
            return n
        if not node:
            return None
        return clonegraph(node, {})