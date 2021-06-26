# Спринт 16
# Задача E. Является ли деревом поиска

class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def is_search_tree(Node):
    if not Node:
        return True
    print(Node.value)
    if Node.left and not Node.left.value < Node.value:
        return False
    if Node.right and not Node.value < Node.right.value:
        return False
    
    return is_search_tree(Node.left) and is_search_tree(Node.right)


def solution(root: Node) -> bool:

    return is_search_tree(root)


if __name__ == '__main__':
    
    left = Node(1)
    right = Node(5)

    node_left = Node(3, left, right)
    node_right = Node(8)
    root = Node(5, node_left, node_right)
    
    
    print(solution(root))