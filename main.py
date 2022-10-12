"""This is the main file"""


class Node:
    """This class is for creating new Node"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """This class is for creating doubly linked list"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0
        self.new_head = None
        self.new_tail = None
        self.new_size_ = 0

    def append(self, data):
        """this function is for adding an element to our main list"""

        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.size_ += 1
            return

        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.size_ += 1

    def append_2nd_list(self, data):
        """this function is for adding an element to our main list"""

        if self.new_head is None:
            self.new_head = Node(data)
            self.new_tail = self.new_head
            self.new_size_ += 1
            return

        self.new_tail.next = Node(data)
        self.new_tail.next.prev = self.new_tail
        self.new_tail = self.new_tail.next
        self.new_size_ += 1

    def begin(self):
        """This function returns elements from the beginning"""

        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def end(self):
        """This function returns elements from the end"""

        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev

    def emplace(self, index, data):
        """"This function emplace the element at the given index"""

        if index > self.size_ or index < 0:
            raise ValueError(f"Index out of range: {index}, size: {self.size_}")
        if index == self.size_:
            self.append(data)
            return
        if index == 0:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev
            self.size_ += 1
            return
        start = self.head
        for _ in range(index):
            start = start.next
        start.prev.next = Node(data)
        start.prev.next.prev = start.prev
        start.prev.next.next = start
        start.prev = start.prev.next
        self.size_ += 1
        return

    def remove(self, index):
        """This function removes element by index"""

        if index >= self.size_ or index < 0:
            raise ValueError(f"Index out of range: {index}, size: {self.size_}")
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.size_ -= 1
            return
        elif index == self.size_ - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size_ -= 1
            return
        if index != 0 and self.new_size_ > index > 0:
            start = self.head
            for _ in range(index):
                start = start.next
            start.prev.next, start.next.prev = start.next, start.prev
            self.size_ -= 1
            return

    def front(self):
        """This function access the first element."""
        print(self.head.data)

    def back(self):
        """This function access the last element."""
        print(self.tail.data)

    def push_back(self, data):
        """This function is for adding an element to the end"""

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
        """This function inserts an element to the beginning"""

        new_node = Node(data)
        if self.size_ == 0 and not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size_ += 1

    def empty(self):
        """This function is for checkin if the list is empty"""

        if self.size_ == 0:
            print("The list is empty.")
        else:
            return

    def size(self):
        """This function returns the number of elements"""
        return self.size_

    def clear(self):
        """This function clears the contents"""

        while self.head is not None:
            self.head = self.head.next
            self.size_ -= 1
        self.size_ = 0
        print("Content cleared. ")

    def insert(self, key, data):
        """"This function inserts the element after the given key"""

        if self.size_ == 0 and not self.head and not self.tail:
            print("Please add some data to your List.")
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node:
                if current_node.data == key:
                    if not current_node.next:
                        current_node.next = new_node
                        new_node.prev = current_node
                        self.tail = new_node
                    else:
                        next_node = current_node.next
                        current_node.next = new_node
                        new_node.prev = current_node
                        new_node.next = next_node
                        next_node.prev = new_node
                    self.size_ += 1
                    return
                else:
                    current_node = current_node.next

    def delete_node(self, node):
        """This function is for deleting duplicate elements"""

        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                if not cur.next:
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    self.head = nxt
                    return
            elif cur == node:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    return
            cur = cur.next

    def unique(self):
        """"This function removes duplicate elements"""

        cur = self.head
        seen = {}
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt
                self.size_ -= 1
        self.print_list()

    def merge(self):
        """Sort list in place."""
        self.head = self.merge_sort(self.head)
        self.print_list()
        print("\n")

    def merge_(self, first, second):
        """This function merges two sorted lists"""

        if first is None:
            return second
        if second is None:
            return first
        if first.data < second.data:
            first.next = self.merge_(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge_(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

    def merge_sort(self, temp_head):
        """Function to do merge sort"""

        if temp_head is None:
            return temp_head
        if temp_head.next is None:
            return temp_head
        second = self.split(temp_head)
        temp_head = self.merge_sort(temp_head)
        second = self.merge_sort(second)
        return self.merge_(temp_head, second)

    def split(self, temp_head):
        """This function splits a doubly linked list into two half-sized dlls"""

        fast = slow = temp_head
        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp

    def splice(self):
        """"This function moves elements from another list"""

        while self.new_head is not None:
            cur = self.new_head.data
            self.push_back(cur)
            self.new_head = self.new_head.next
        self.new_size_ -= 1
        self.print_list()

    def resize(self, size):
        """This function changes the number of elements stored"""

        if size in (0, self.size_):
            print("Nothing changed.")
            self.size_ = self.size_
        elif size < 0:
            print("Size can not be negative")
        elif self.size_ < size:
            while self.size_ < size:
                self.append(0)
        elif self.size_ > size:
            while self.size_ > size:
                self.tail = self.tail.prev
                cur = self.tail.next
                self.delete_node(cur)
                self.size_ -= 1
        self.print_list()

    def print_lst(self, node):
        """This function prints merged list"""
        # temp = node
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print("\n")

    def print_list(self):
        """This function prints our list"""

        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

    def __iter__(self):
        """Implement iter(self)."""
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __eq__(self, other):
        """Implement comparison: a == b."""

        if type(self) is not type(other):
            return False
        if self.size_ != other.size_:
            return False
        for i, j in zip(self, other):
            if i != j:
                return False
        return True

    def __ne__(self, other):
        """Implement comparison: a != b."""

        if type(self) is not type(other):
            return False
        if self.size_ != other.size_:
            return True
        if self.size_ == other.size_:
            for i, j in zip(self, other):
                if i != j:
                    return True
            return False

    def __gt__(self, other):
        """Implement comparison: a > b."""

        if type(self) is not type(other):
            return False
        if self.size_ == other.size_:
            while self.head and other.head:
                if self.head.data > other.head.data:
                    return True
                    self.head = self.head.next
                    other.head = other.head.next
                elif self.head.data < other.head.data:
                    return False
                self.head = self.head.next
                other.head = other.head.next

            # if self.head.data == other.head.data:
            #     return False



        # elif self.size_ > other.size_:
        #     while self.size_ > other.size_:
        #         myList.self.append(0)
        #         self.size_ += 1
        #
        #         return True





if __name__ == "__main__":
    myList = DoublyLinkedList()
    myList.append(1)
    myList.append(2)
    myList.append(12)
    myList.append(4)
    myList.append(5)

    # myList.append_2nd_list(11)
    # myList.append_2nd_list(12)
    # myList.append_2nd_list(13)
    # myList.append_2nd_list(14)
    # myList.append_2nd_list(15)

    myList1 = DoublyLinkedList()
    myList1.append(1)
    myList1.append(2)
    myList1.append(3)
    myList1.append(4)
    myList1.append(5)

    print(myList == myList1)
    print(myList != myList1)
    print(myList > myList1)

    #
    # print("The original list:")
    # myList.print_list()
    # print("Size:", myList.size())
    # print("\n")
    #
    # print("List after changing size")
    # myList.resize(3)
    # print("Size:", myList.size())
    #
    # print("List after adding element from another list")
    # myList.splice()
    # print("Size:", myList.size())
    # print("\n")
    #
    # print("The first element of the list is:", end=' ')
    # myList.front()
    #
    # print("The last element of the list is:", end=' ')
    # myList.back()
    #
    # print("returns the list from the beginning:")
    # myList.begin()
    #
    # print("returns the list from the end:")
    # myList.end()
    # myList.remove(3)
    # myList.push_back(1100)
    # myList.push_front(125)
    # myList.insert(21, 4)
    # myList.insert(321, 17)
    # myList.emplace(3, 3)
    #
    # print("Changed list:")
    # myList.print_list()
    # print("Size:", myList.size())
    #
    # print("List after sorting")
    # myList.merge()
    # print("Size:", myList.size())
    #
    # print("Unique elements:")
    # myList.unique()
    # print("Size:", myList.size())
    #
    # print("\n")
    #
    # myList.clear()
    # print("Size:", myList.size())
    # myList.print_list()
    # myList.empty()
