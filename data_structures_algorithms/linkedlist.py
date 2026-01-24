class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_list(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def print_linkedlist(self):
        if self.head == None:
            print("LinkedList is Empty")
            return
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
            



if __name__ == '__main__':
    llist = LinkedList()
    llist.append_list(3)
    llist.append_list(1)
    llist.append_list(4)
    llist.print_linkedlist()
