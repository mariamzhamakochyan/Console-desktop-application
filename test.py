import main
if __name__ == "__main__":
    myList = DoublyLinkedList()
    myList.append(113)
    myList.append(21)
    myList.append(3)
    myList.append(12)
    myList.append(321)

    myList.append_2nd_list(11)
    myList.append_2nd_list(12)
    myList.append_2nd_list(13)
    myList.append_2nd_list(14)
    myList.append_2nd_list(15)
    #
    # # myList.splice_by_index(2)
    # # myList.print_list()
    # # print("\n")
    #
    print("The original list:")
    myList.print_list()
    print("Size:", myList.size())
    print("\n")

    print("List after changing size")
    myList.resize(7)
    myList.print_list()
    print("\n")
    print("Size:", myList.size())

    print("List after adding element from another list")
    myList.splice()
    myList.print_list()
    print("Size:", myList.size())
    print("\n")

    print("The first element of the list is:", end=' ')
    myList.front()

    print("The last element of the list is:", end=' ')
    myList.back()

    print("returns the list from the beginning:")
    myList.begin()

    print("returns the list from the end:")
    myList.end()
    myList.remove(3)
    myList.push_back(1100)
    myList.push_front(125)
    myList.insert(21, 4)
    myList.insert(321, 17)
    myList.emplace(3, 3)

    print("Changed list:")
    myList.print_list()
    print("Size:", myList.size())

    myList.head = myList.merge_sort(myList.head)
    print("List after sorting")
    myList.print_lst(myList.head)

    print("Unique elements:")
    myList.unique()
    myList.print_list()
    print("\n")

    myList.clear()

    print("Size:", myList.size())
    myList.empty()
