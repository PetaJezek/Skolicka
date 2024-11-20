class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self, root = None) -> None:
        self.root = root
    def hloubka(self) -> int:
        def _height(node):
            return 0 if node is None else(
                max(self.hloubka(self.root.left), self.hloubka(self.root.right)) +1
            )
        return _height(self.root)

    def zreflektuj(self):
        def _zreflektuj(node):
            if node is None: 
                return
            _zreflektuj(node.left)
            _zreflektuj(node.right)
           
            temp = node.right
            node.right = node.left
            node.left = temp
        _zreflektuj(self.root)
            