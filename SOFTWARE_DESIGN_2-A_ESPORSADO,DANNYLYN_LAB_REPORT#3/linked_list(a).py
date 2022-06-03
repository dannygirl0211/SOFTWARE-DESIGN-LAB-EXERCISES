
class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


class singly_linked_list:
    def __init__(self):
        self.head_val = None

    def list_print(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data_val)
            print_val = print_val.next_val

    def at_beginning(self, newdata):
        new_node = Node(newdata)

        new_node.next_val = self.head_val
        self.head_val = new_node

    def at_end(self, newdata):
        new_node = Node(newdata)
        if self.head_val is None:
            self.head_val = new_node
            return
        laste = self.head_val
        while (laste.next_val):
            laste = laste.next_val
        laste.next_val = new_node

    def remove_node(self,removekey):
        head_val = self.head_val

        if(head_val is not None):
            if (head_val == removekey):
                self.head_val = head_val.next_val
                head_val = None
                return
        while (head_val is not None):
            if head_val.data_val == removekey:
                break
            prev = head_val
            head_val = head_val.next_val

            if (head_val== None):
                return

            prev.next_val = head_val.next_val
            head_val = None


list = singly_linked_list()
list.head_val = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.head_val.next_val = e2
e2.next_val = e3

list.at_beginning("Sun")
list.at_end("Thu")
list.remove_node("Mon")
list.list_print()
