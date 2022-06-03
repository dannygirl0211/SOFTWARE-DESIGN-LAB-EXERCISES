
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


root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)
print(root.find_val(11))
