
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def find_val(self, val):
        if val < self.data:
            if self.left is None:
                return str(val) + " Not Found"
            return self.left.find_val(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + " Not Found"
            return self.right.find_val(val)
        else:
            print(str(self.data) + ' is found')


    def print_tree(self):
       if self.left:
           self.left.print_tree()
       print(self.data),
       if self.right:
           self.right.print_tree()


    def pre_order_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order_traversal(root.left)
            res = res + self.pre_order_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res = res + self.post_order_traversal(root.right)
            res.append(root.data)
        return res

    def in_order_traversal(self, root):
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.data)
            res = res + self.in_order_traversal(root.right)
        return res


root = Node(40)
root.insert(20)
root.insert(60)
root.insert(10)
root.insert(30)
root.insert(50)
root.insert(70)
print(root.pre_order_traversal(root))
print(root.post_order_traversal(root))
print(root.in_order_traversal(root))

