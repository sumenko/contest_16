# Спринт 16
# Задача А. Лампочки

class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def get_max(Node, max_lamp = None):
    if not Node:
        return max_lamp

    if not Node.left and not Node.right:
        return Node.value

    if not max_lamp: max_lamp = Node.value
    return max(Node.value, get_max(Node.left, max_lamp), get_max(Node.right, max_lamp))


def solution(Node) -> int:
    return get_max(Node)
    

if __name__ == '__main__':
    left_1 = Node(14)
    right_1 = Node(1)
    left_root = Node(8, left_1, right_1)
    
    left_2 = Node(10)
    right_2 = Node(5)
    right_root = Node(1, left_2, right_2)
    root2 = Node(100, left_root, right_root) 
    print(solution(root2))
