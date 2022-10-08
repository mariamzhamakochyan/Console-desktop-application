'''This is the main file'''

class Node:
    '''This class is intended to represent a doubly linked list'''
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    '''This class is for our functions '''        

    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0
        
 
    
    def push_back(self, data):
        '''This function is for adding an element to the end'''
        
        new_node = Node(data)
        if self.size_ == 0 and not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size_ += 1
        
    def push_front(self, data):
        '''This function inserts an element to the beginning'''
        
        new_node = Node(data)
        if self.size_== 0 and not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 
        self.size_ += 1

       
    def traverse_fw(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def empty(self):
        '''This function is for checkin if the list is empty'''
        
        if self.size_ == 0 and not self.head and not self.tail:
            print("The list is empty.")
        else:
            return
            
    def size(self):
        '''This function returns the number of elements'''
        return self.size_  
    
    def clear(self):
        '''This function clears the contents'''
        
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size_ -=1
        print("Content cleared. ")

        

if __name__ == "__main__":
    myList = DoublyLinkedList()
    myList.push_back(1)
    myList.push_back(2)
    myList.push_back(3)
    myList.empty()
    print()
    myList.traverse_fw()
    print()
    print("Size:", myList.size())
    myList.clear()
    print()
    print("Size:", myList.size())
