class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def prointer(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def delete(self,key):
        temp = self.head
        pr = None

        if temp and temp.data!=key:
            pr = temp
            temp = temp.next
        if temp and temp.data==key:
            self.head = temp.next
            temp = None
            return
        pr.next = temp.next
        temp = None




l1 = linkedlist()
l1.head = node(5)
l1.append(2)
l1.append(3)
l1.delete(10)
l1.prointer()