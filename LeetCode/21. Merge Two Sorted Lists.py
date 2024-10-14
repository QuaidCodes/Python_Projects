# 21. Merge Two Sorted Lists
# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
def mergeTwoLists(lst1, lst2):
    new_list = []
    curr_val = None
    lst1_node = lst1
    lst2_node = lst2


    condition = False
    while not condition:
        if lst1_node:
            new_list.append(lst1_node.val)
            lst1_node = lst1_node.next
            print(lst1_node.val, lst2_node.val)
        elif lst2_node:
            new_list.append(lst2_node.val)
            lst2_node = lst2_node.next
            print(lst1_node.val, lst2_node.val)
        else:
            return new_list.sort()

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node1.next = node2
node2.next = node3

node_1 = ListNode(1)
node_2 = ListNode(3)
node_3 = ListNode(4)

node_1.next = node_2
node_2.next = node_3

print(mergeTwoLists(node1, node_1))
