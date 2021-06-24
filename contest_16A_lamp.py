# Спринт 16
# Задача А. Лампочки

class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def solution(Node) -> int:
    max_value = 0
    while 1:
        
        max_value = max(max_value, new_value)


if __name__ == '__main__':
    # my_solution.py
    left = Node(3)
    right = Node(5)
    root = Node(1, left, right)
    
