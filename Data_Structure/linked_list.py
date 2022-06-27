class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_middle(self, data, pos):
        new_node = Node(data)

        if pos < 0 or pos > self.get_length():
            raise Exception('Invalid Position')

        if pos == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        c = 0
        while itr.next:
            if c == pos-1:
                new_node = Node(data, itr.next)
                itr.next = new_node
                break
            itr = itr.next
            c += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def remove_at(self, pos):
        if pos < 0 or pos > self.get_length():
            raise Exception('Invalid Position')

        if pos == 0:
            self.head = self.head.next
            return

        itr = self.head
        c = 0
        while itr.next:
            if c == pos-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            c += 1

    def print_linkedlist(self):
        itr = self.head

        lt_str = ''
        while itr:
            lt_str += str(itr.data) + ('-->' if itr.next else '')
            itr = itr.next
        print(lt_str)

    def get_length(self):
        c = 0
        itr = self.head
        while itr:
            c += 1
            itr = itr.next
        return c

    def insert_values(self, data_list):
        self.head = None
        for d in data_list:
            self.insert_at_end(d)

root = Linked_List()
root.insert_at_beginning(6)
root.insert_at_end(61)
root.insert_at_end(610)
# root.insert_at_middle(23, 1)
# print(root.get_length())
# root.remove_at(0)
# root.insert_values([3, 45, 58])
root.print_linkedlist()