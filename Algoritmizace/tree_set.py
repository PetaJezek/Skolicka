class Node():
    def __init__(self, value = None, right = None, left = None):
        self.right = right
        self.left = left
        self.value = value
    
class TreeSet():
    def __init__(self, root: Node):
        self.root = None
    def contains(self, x: int):
        contains = False
        current_node = self.root
        while contains == False:
            if current_node.value == None:
                break
            elif x == current_node.value:
                contains = True
            elif x > current_node.value:
                current_node = current_node.right
            elif x < current_node.value:
                current_node = current_node.left
        return contains
    def add(self, x: int):
        if self.contains(x):
            return
        else:
            current_node = self.root
            while True:
                if current_node.value == None:
                    current_node.value = x
                    break
                elif x > current_node.value:
                    current_node = current_node.right
                elif x < current_node.value:
                    current_node = current_node.left
        return
    def remove(self, x: int):
        if self.contains(x):
            current_node = self.root
            parent = None

            while True:
                if x == current_node.value:
                    while

        else:
            return
   
    
            
