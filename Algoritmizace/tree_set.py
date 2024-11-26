class Node():
    def __init__(self, value = None, right = None, left = None):
        self.right = right
        self.left = left
        self.value = value
    
class TreeSet():
    def __init__(self):
        self.root = None
        self.size_number = 0
    def contains(self, x: int):
        contains = False
        current_node = self.root
        
        while contains == False:
            if current_node == None:
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
        
        if self.root == None:
                self.root = Node(x)
                self.size_number += 1
        else:
            self.size_number += 1
            current_node = self.root
            while True:
                if x < current_node.value:
                    if current_node.left == None:
                        current_node.left = Node(x)
                        break
                    else:
                        current_node = current_node.left
                elif x > current_node.value:
                    if current_node.right == None:
                        current_node.right = Node(x)
                        break
                    else:
                        current_node = current_node.right
    def remove(self, x: int):
        if self.contains(x):
            current_node = self.root
            parent = None
            while current_node.value != x:
                if current_node.value > x:
                    parent = current_node
                    current_node = current_node.left
                else:
                    parent = current_node
                    current_node = current_node.right

            if current_node.left != None and current_node.right != None:
                temp_node = current_node.right
                temp_parent = current_node
                Left = False
                while temp_node.left != None:
                    temp_parent = temp_node
                    temp_node = temp_node.left
                    Left = True
                    
                current_node.value = temp_node.value
                if Left:
                    temp_parent.left = temp_node.right
                else:
                    temp_parent.right = temp_node.right
            elif current_node != self.root:
                if current_node.left == None and current_node.right == None:
                    if parent.left == current_node:
                        parent.left = None
                    else:
                        parent.right = None
                elif current_node.left == None:
                    if parent.left == current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                else:
                    if parent.left == current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
            else:
                if self.root.left != None:
                    self.root = self.root.left
                elif self.root.right != None:
                    self.root = self.root.right
                else:
                    self.root = None
            self.size_number -= 1
            return
        else:
            pass      
    def min(self):
        if self.root == None:
            return None
        else:
            current_node = self.root
            while current_node.left != None:
                current_node = current_node.left
            return current_node.value
    def max(self):
        if self.root == None:
            return None
        else:
            current_node = self.root
            while current_node.right != None:
                current_node = current_node.right
            return current_node.value
    def size(self):
        return self.size_number
    def count(self, lo: int, hi: int):
        return self._count(self.root, lo, hi)  
    def _count(self, current_node: Node, lo: int, hi: int):
        if current_node == None:
            return 0
        if current_node.value >= lo and current_node.value <= hi:
            return 1 + self._count(current_node.left, lo, hi) + self._count(current_node.right, lo, hi)
        elif current_node.value < lo:
            return 0 + self._count(current_node.right, lo, hi)
        elif current_node.value > hi:
            return 0 + self._count(current_node.left, lo, hi)

