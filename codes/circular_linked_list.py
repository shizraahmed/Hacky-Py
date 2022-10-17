# first we create the class Node, this represents the elements in the list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# this class represents the list, the head is the first element in the list


class CircularLinkedList():
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, data):
        # first case: the list is empty and since we only have the head, it will be the first and last element so it will point to herself.
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            newNode = Node(data)
            pointer = self.head
            while pointer.next != self.head:
                pointer = pointer.next
            newNode.next = self.head
            pointer.next = newNode
        self._size += 1

    def remove(self, key):
        # first case: the list is empty
        if not self.head:
            return 'Empty list'

        # second case: when there's only one element in the list (the head)
        elif self.head.data == key and self.head.next == self.head:
            self.head = None

        # third case: when we have more than one element in the list and we want to remove the head
        elif self.head.data == key:
            pointer = self.head
            while pointer.next != self.head:
                pointer = pointer.next
            pointer.next = self.head.next
            self.head = self.head.next
        # fourth case: remove any other element instead of the head
        else:
            pointer = self.head.next
            previous = self.head
            while pointer.data != key:
                if pointer.next == self.head:
                    return 'Element does not exist in list'
                else:
                    previous = pointer
                    pointer = pointer.next
            previous.next = pointer.next
            pointer.next = None
            pointer = None
        self._size -= 1

# this method prints the list
    def __repr__(self):
        r = ''
        pointer = self.head
        while pointer.next != self.head:
            r = r + str(pointer.data) + ','
            pointer = pointer.next
        r = r + str(pointer.data)
        return r

    def __str__(self):
        if self.head:
            return self.__repr__()
        else:
            return 'empty list'

    def __len__(self):
        return self._size

# myList = CircularLinkedList()
# myList.append(1)
# myList.append('python')
# print(myList)
# print(len(myList))
# myList.remove(1)
# print(myList)
