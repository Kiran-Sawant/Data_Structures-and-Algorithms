class node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.start = None

    def insertLast(self, value):
        newNode = node(value)

        if(self.start == None):
            self.start = newNode
        else:
            temp = self.start
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode

    def deleteFirst(self):

        if self.start == None:
            print("List is empty")
        else:
            # Python has automatic garbage collection. Therefore,
            # if no value is assigned to first node in memory, it will automatically be cleared
            self.start = self.start.next

    def viewList(self):

        if self.start == None:
            print("List is Empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next

myList = LinkedList()
myList.insertLast(10)
myList.insertLast(11)
myList.insertLast(12)
myList.insertLast(13)

myList.viewList()
print()
myList.deleteFirst()

myList.viewList()