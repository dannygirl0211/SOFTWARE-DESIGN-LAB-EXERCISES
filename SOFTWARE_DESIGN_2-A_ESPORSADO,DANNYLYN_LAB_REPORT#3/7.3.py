
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def get_count_rec(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.get_count_rec(node.next)

    def get_count(self):
        return self.get_count_rec(self.head)


if __name__ == '__main__':
    llist = linked_list()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print('Count of nodes is :', llist.get_count())
