'''This class is intended to represent a doubly linked list'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def push_front(self, data):
        '''new head node'''
        
        new_node = Node(data)
        # check if the list is empty
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = new_node
            self.__tail = new_node
        else:
            # when there is atleast one node
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node  # new_node is our new head node
        self.__size += 1
    def push_back(self, data):
        new_node = Node(data)
        # check if the list is empty
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node  # new_node is our new tail node
        self.__size += 1
    
    def traverse_fw(self):
        current_node = self.__head
        while current_node:   # while the current node is not None
            print(current_node.data)
            current_node = current_node.next
    
    def remove_if(self, data):
        # when there is no node
        if self.__size == 0 and not self.__head and not self.__tail:  # the code should work without checking for head and tail nodes
            print("No data to remove")
        # when the list contains 1 node
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
            self.__size -= 1
        # when the list contains more than one node
        elif self.__size > 1:
            current_node = self.__head
            previous_node = None
            while current_node:  # while the current node is not None
                if current_node.data == data:
                    # removing the head node
                    if not previous_node:
                        next_node = current_node.next
                        next_node.prev = None   # the head always points towards a None
                        current_node.next = None
                        del current_node
                        self.__head = next_node
                    # removing the tail node
                    elif not current_node.next:  # when the next node to the current node is a None (tail node)
                        previous_node.next = None
                        current_node.prev = None
                        del current_node
                        self.__tail = previous_node
                    # removing any random node BUT not the head and the tail nodes
                    else:
                        next_node = current_node.next
                        current_node.prev = None
                        current_node.next = None
                        del current_node
                        previous_node.next = next_node
                        next_node.prev = previous_node
                    self.__size -= 1
                    return   # avoiding an infinite loop
                else:
                    # traversing to the next node
                    # if the data is not matched
                    previous_node = current_node
                    current_node = current_node.next

    def traverse_bw(self):
        current_node = self.__tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev
        
    
    def add_before(self, key, data):
        # check for empty data structure
        if self.__size == 0 and not self.__head and not self.__tail:
            print("Please add some data to your List.")
        else:
            # when we have atleast one node
            new_node = Node(data)
            current_node = self.__head
            previous_node = None
            while current_node:
                # add before the head node
                if current_node.data == key:
                    if not previous_node:  # if the previous node is None
                        new_node.next = current_node
                        current_node.prev = new_node
                        self.__head = new_node  # the "new_node" is our new head node
                    else:
                        # adding before any node BUT the head node
                        previous_node.next = new_node
                        new_node.prev = previous_node
                        new_node.next = current_node
                        current_node.prev = new_node
                    self.__size += 1
                    return   # to avoid infinite loop
                else:
                    # if the data does not match
                    previous_node = current_node
                    current_node = current_node.next

    def add_after(self, key, data):
        # check for empty data structure
        if self.__size == 0 and not self.__head and not self.__tail:
            print("Please add some data to your List.")
        else:
            # when we have atleast one node
            new_node = Node(data)
            current_node = self.__head
            while current_node:
                if current_node.data == key:
                    # add after the tail node
                    if not current_node.next:  # if "current_node.next" points to None
                        current_node.next = new_node
                        new_node.prev = current_node
                        self.__tail = new_node  # new node is not the tail node of our list
                    else:
                        # adding after any node BUT the tail node
                        next_node = current_node.next
                        current_node.next = new_node
                        new_node.prev = current_node
                        new_node.next = next_node
                        next_node.prev = new_node
                    self.__size += 1
                    return   # to avoid infinite loop
                else:
                    current_node = current_node.next    
                    
        
    def list_size(self):
        return self.__size   
        
    
    def deleteNode(head_ref,del_):

	# base case
	if head_ref == None or del_ == None:
	    return head_ref

	# If node to be deleted is head node
	if (head_ref == del_):
		head_ref = del_.next

	# Change next only if node to be deleted
	# is NOT the last node
	if (del_.next != None):
		del_.next.prev = del_.prev

	# Change prev only if node to be deleted
	# is NOT the first node
	if (del_.prev != None):
		del_.prev.next = del_.next
	return head_ref   
        
    def removeDuplicates( head_ref):

	# if DLL is empty or if it contains only
	# a single node
	if ((head_ref) == None or (head_ref).next == None):
		return head_ref

	ptr1 = head_ref
	ptr2 = None

	# pick elements one by one
	while(ptr1 != None) :
		ptr2 = ptr1.next

		# Compare the picked element with the
		# rest of the elements
		while (ptr2 != None):
		
			# if duplicate, then delete it
			if (ptr1.data == ptr2.data):
			
				# store pointer to the node next to 'ptr2'
				next = ptr2.next

				# delete node pointed to by 'ptr2'
				head_ref = deleteNode(head_ref, ptr2)

				# update 'ptr2'
				ptr2 = next

			# else simply move to the next node
			else:
				ptr2 = ptr2.next
		ptr1 = ptr1.next
	return head_ref

# Function to insert a node at the beginning
# of the Doubly Linked List
def push( head_ref, new_data):

	# allocate node
	new_node = Node()

	# put in the data
	new_node.data = new_data

	# since we are adding at the beginning,
	# prev is always None
	new_node.prev = None

	# link the old list off the new node
	new_node.next = (head_ref)

	# change prev of head node to new node
	if ((head_ref) != None):
		(head_ref).prev = new_node

	# move the head to point to the new node
	(head_ref) = new_node
	return head_ref

# Function to print nodes in a
# given doubly linked list
def printList( head):

	# if list is empty
	if (head == None):
		print("Doubly Linked list empty")

	while (head != None):
		print( head.data ,end= " ")
		head = head.next
    
        
if __name__ == "__main__":
    myList = Doubly()
    myList = Doubly()
    myList = Doubly()
    myList.push_back(1)
    myList.push_back(2)
    myList.push_back(3)

    myList.push_front(0)
    myList.push_front(-1)
    myList.push_front(-2)

    myList.add_before(-2, -3)
    myList.add_before(0, -0.5)
    myList.remove_if(-3)
    myList.remove_if(0)
    myList.remove_if(4)
    
    head=removeDuplicates(head)
    print("\nDoubly linked list after removing duplicates:")
    printList(head)

    myList.add_after(3, 4)
    myList.add_after(0, 0.5)
    myList.traverse_fw()
    print()
    print("Size:", myList.list_size())
    # myList.traverse_bw()
    # print()
