
import enum
# Red is True
# Black is False
class Color(enum.Enum):
    RED = True
    BLACK = False

# Node creation
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.color : Color = Color.RED #defult red

    def __repr__(self):
        return f'Node(val={self.val}, color={self.color.value}, left={self.left}, right={self.right})'



class RBT:
    def __init__(self):
        self.root = None

    def isRed(self, Node):
        if Node == None:
            return False
        return Node.color == Color.RED
    
    def flip_color(self,node):
        node.color = Color.RED
        node.left.color = Color.BLACK
        node.right.color = Color.BLACK
    def rotate_left(self, node):

        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        new_root.color = node.color
        node.color = Color.RED
        return new_root
    def rotate_right(self, node):

        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        new_root.color = node.color
        node.color = Color.RED
        return new_root

    def insert(self, value):
        # insertion and updation of root
        self.root = self.__insert(self.root, value)
        self.root.color = Color.BLACK
    def __insert(self, root, value):
        # Recursive insertion of the root
        if root == None:
            return Node(value)
        
        if value < root.value:
            root.left = self.__insert(root.left, value)
        elif value > root.value:
            root.right = self.__insert(root.right, value)
        else:
            root.value = value
        

        #is rotation or color needed
        if self.isRed(root.right) and not self.isRed(root.left):
            root = self.rotate_left(root)
        if self.isRed(root.left) and self.isRed(root.left.left):
            root = self.rotate_right(root)
        if self.isRed(root.left) and self.isRed(root.right):
            self.flip_color(root)


        return root




    def inorder(self) -> None:
        """Inorder Traversal for root"""
        self.__inorder(self.root)

    def __inorder(self, root: Node) -> None:
        """Recursive Inorder Traversal for any node"""
        if root is None:
            return
        self.__inorder(root.left)
        print(root.value, end=" ")
        self.__inorder(root.right)


rbt = RBT()
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(40)
rbt.insert(50)
rbt.insert(25)
rbt.inorder()