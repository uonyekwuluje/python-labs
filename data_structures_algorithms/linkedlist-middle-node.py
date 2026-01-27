class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linkedlist(self):
        if self.head == None:
            print("Linkedlist is Empty")
            return
        else:
            temp = self.head
            while temp:
                if temp.next != None:
                    print(temp.data,end=" -> ")
                else:   
                    print(temp.data)
                temp = temp.next

    def append_linkedlist(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def find_middle_linkedlist(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer    


if __name__ == '__main__':
    llist = LinkedList()
    llist.append_linkedlist(1)
    llist.append_linkedlist(2)
    llist.append_linkedlist(3)
    llist.append_linkedlist(4)
    llist.append_linkedlist(5)
    llist.append_linkedlist(6)
    llist.append_linkedlist(7)
    llist.append_linkedlist(8)
    llist.print_linkedlist()
    print(f"Middle Node is => {llist.find_middle_linkedlist().data}")
