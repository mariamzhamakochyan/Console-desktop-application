from main import Node
from main import DoublyLinkedList

"""That's how we creat lists."""
myList = DoublyLinkedList()
myList1 = DoublyLinkedList()
myList2 = DoublyLinkedList()


"""We append elements to our list,called myList"""
myList.append(1)
myList.append(12)
myList.append(3)
myList.append(400)
myList.append(5)

myList1.append(1)
myList1.append(2)
myList1.append(3)
myList1.append(4)
myList1.append(5)

""" '==' operator is checking if two lists are equal, and return a boolean value (True or False)"""
print("Boolean value for '=='")
print(myList == myList1)

""" '!=' operator is checking if two lists are NOT equal, and return a boolean value (True or False)"""
print("Boolean value for '!='")
print(myList != myList1)

""" '>' operator is checking if our first list is grater than the second one. Return a boolean value (True or False)"""
print("Boolean value for '>'")
print(myList > myList1)

""" '<' operator is checking if our first list is smaller than the second one. Return a boolean value (True or False)"""
print("Boolean value for '<'")
print(myList < myList1)

""" '>=' operator is checking if our first list is grater or equal to
 the second one. Return a boolean value (True or False)"""
print("Boolean value for '>='")
print(myList >= myList1)

""" '<=' operator is checking if our first list is smaller or equal to
 the second one. Return a boolean value (True or False)"""
print("Boolean value for '<='")
print(myList <= myList1)

""" '+' operator is the sum of two lists """
print("output '+'")
print(myList + myList1)

""" '<<' operator returns myList
 with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). 
 This is the same as multiplying myList by 2**y. (in that case y = 1)"""
print("output '<<'")
print(myList << 1)

""" '+=' operator adds the values of the second to the first list."""
print("output '+='")
myList += myList1
myList.print_list()
print("\n")

print("The original list:")
myList.print_list()
print("Size:", myList.size())
# print("\n")

print("List after adding element from another list")
myList.splice(myList1)
print("Size:", myList.size())
# print("\n")

print("The first element of the list is:", end=' ')
"""This function return the first element of the list"""
myList.front()

print("The last element of the list is:", end=' ')
"""This function return the last element of the list"""
myList.back()

print("returns the list from the beginning:")
"""This func return the list from the beginning"""
myList.begin()

print("returns the list from the end:")
"""This func return the list from the end"""
myList.end()

"""Removing list elements by index.
if index is negative or grater than our list size,
we will have a ValueError"""
myList.remove(3)

"""This function is for adding an element to the end"""
myList.push_back(1100)

"""This function is for adding an element to the beginning"""
myList.push_front(125)

"""Insert element after given element. 
If element does not exist nothing will be inserted"""
myList.insert(125, 4)
myList.insert(321, 17)

""""This function emplace the element at the given index.
if index is greater or negative, we will have a ValueError"""
myList.emplace(3, 3)

print("Changed list:")
myList.print_list()
print("Size:", myList.size())

print("List after sorting")
"""This function merges two lists"""
myList.merge()
print("Size:", myList.size())

print("Unique elements:")
"""This function returns unique elements"""
myList.unique()
print("Size:", myList.size())

"""resize() function change our list size, if its < 0 
we have message that size can not be negative.If it = 0 our lst will be cleared"""
print("List after changing size")
myList.resize(3)
print("Size:", myList.size())

"""This function clear our list"""
myList.clear()
print("Size:", myList.size())
myList.print_list()
"""We check if list is cleared and is empty """
myList.empty()
