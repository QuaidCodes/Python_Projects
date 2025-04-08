
# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_node(self, data, index):
        new_node = Node(data)
        curr_node = self.head
        position = 0

        if position == index:
            self.insert_at_beginning(data)
        else:
            while (curr_node != None and position+1 != index):
                position += 1
                curr_node = curr_node.next

            if curr_node != None:
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print("Index not present")

    def insert_at_end(self, data):
        new_node = Node(data)

        curr_node = self.head

        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node

    def print_list(self):
        curr_node = self.head

        while curr_node.next:
            print(curr_node.data)
            curr_node = curr_node.next

    def print_end(self):
        curr_node = self.head

        while curr_node.next:
            curr_node = curr_node.next

        print(curr_node.data)

    def get_head(self):
        print(self.head.data)

linked_list = LinkedList()
linked_list.insert_at_beginning("Head")
linked_list.insert_at_end("End")

print("List")
linked_list.print_list()







