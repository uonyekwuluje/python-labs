class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linkedlist(self):
        if self.head == None:
            print("Linkedlist is empty")
        else:
            temp = self.head
            while temp:
                if temp.next != None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data)
                temp = temp.next
        return        
 
    def append_linkedlist(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        return

    def prepend_linkedlist(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        return    

    def poplast_linkedlist(self):
        if self.head == None:
            print("Linkedlist is Empty")
            return
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            return
    
    def listlenght_linkedlist(self):
        if self.head == None:
            print("Empty Linkedlist")
            return
        else:
            count = 0
            temp = self.head
            while temp:
                count += 1
                temp = temp.next
        return count        

    def getvalue_linkedlist(self,value):
        if self.head == None:
            print("Empty Linkedlist")
            return
        else:
            count = 0
            temp = self.head
            while temp:
                if temp.data == value:
                    return f"{value} Found in Linkedlist index {count}"
                count += 1
                temp = temp.next
        return f"{value} Not Found in Linkedlist"        

    def setvalue_linkedlist(self,index,value):
        if self.head == None:
            print("Empty Linkedlist. Appending Value")
            self.append_linkedlist(value)
            return
        else:
            new_node = Node(value)
            count = 0
            curr = self.head
            while curr:
                if count == index:
                    curr.data = value
                curr = curr.next
                count += 1






if __name__ == '__main__':
    llist = LinkedList()
    llist.print_linkedlist()
    llist.append_linkedlist(4)
    llist.append_linkedlist(5)
    llist.append_linkedlist(1)
    llist.append_linkedlist(7)
    llist.append_linkedlist(8)
    llist.append_linkedlist(6)
    llist.print_linkedlist()
    llist.prepend_linkedlist(120)
    llist.prepend_linkedlist(20)
    llist.prepend_linkedlist(15)
    llist.print_linkedlist()
    llist.poplast_linkedlist()
    llist.print_linkedlist()
    print(f"The Lenght of the linkedlist => {llist.listlenght_linkedlist()}")
    search_item = 7
    print(llist.getvalue_linkedlist(search_item))
    llist.setvalue_linkedlist(4,99)
    llist.print_linkedlist()
