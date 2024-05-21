class DoublyLinkedListNode:
    def __init__(self, _data):
        self.data = _data
        self.next: DoublyLinkedListNode = None
        self.prev: DoublyLinkedListNode = None

    def __repr__(self) -> str:
        return f"<node_data = {self.data}>"


class LinkedListIterator:
    def __init__(self, _node: DoublyLinkedListNode):
        self.current_node = _node

    def __next__(self):
        current_node = self.current_node
        if current_node is None:
            raise StopIteration
        next_node = self.current_node.next
        self.current_node = next_node
        return current_node.data

    def current(self):
        return self.current_node


class DoublyLinkedList:
    iter_class = LinkedListIterator
    node_class = DoublyLinkedListNode

    def __init__(self, *args):
        self.head: self.node_class = None
        self.tail: self.node_class = None
        self.length = 0
        if len(args):
            for data in args:
                self.insert_last(data)
            self.length = len(args)
        self.itr_obj = self.iter_class(self.head)

    def __iter__(self):
        self.itr_obj = self.iter_class(self.head)
        return self.itr_obj

    def __repr__(self):
        linked_list_repr = ""
        for node_data in self:
            linked_list_repr += f"({node_data}) "
        return f"linked_list -{(str(self.length))}-> |{self.head and self.head.data}| {linked_list_repr} |{self.tail and self.tail.data}|"

    def __len__(self):
        return self.length

    def insert_last(self, _data):
        # create new_node contain _data
        # check if the list is empty
        # then make the new_node be the head and the tail
        # else make tail.next be the new_node and the new_node.prev be the tail
        # then make the new_node be the tail
        # increase the list length
        new_node = self.node_class(_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length = self.length + 1
        return new_node

    def insert_head(self, _data):
        # create new_node contain _data
        # check if the list is empty
        # then make the new_node be the head and the tail
        # else make new_node.next be the head
        # then make the new_node be the head
        # increase the list length
        new_node = self.node_class(_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length = self.length + 1
        return new_node

    def find_node(self, _data) -> DoublyLinkedListNode:
        # search about the node contian _data return None if not found it
        current_node = self.head
        for node_data in self:
            if _data == node_data:
                return current_node
            current_node = current_node.next
        return None

    def insert_before(self, _data_to_insert, _data_to_find):
        ref_node = self.find_node(_data_to_find)
        new_node = self.node_class(_data_to_insert)
        if ref_node is None:
            raise ValueError(f"list doesn't contain this value '{_data_to_find}'")
        if ref_node == self.head:
            new_node = self.insert_head(_data_to_insert)
        else:
            new_node.next = ref_node
            new_node.prev = ref_node.prev
            ref_node.prev.next = new_node
            ref_node.prev = new_node
            self.length += 1
        return new_node

    def insert_after(self, _data_to_insert, _data_to_find):
        ref_node = self.find_node(_data_to_find)
        new_node = self.node_class(_data_to_insert)
        if ref_node is None:
            raise ValueError(f"list doesn't contain this value '{_data_to_find}'")
        if ref_node == self.tail:
            new_node = self.insert_last(_data_to_insert)
        else:
            new_node.next = ref_node.next
            new_node.prev = ref_node
            ref_node.next.prev = new_node
            ref_node.next = new_node
            self.length += 1
        return new_node

    def delete_node(self, _node: DoublyLinkedListNode):
        if _node is None:
            raise ValueError("node can't be None")
        if self.tail == self.head and _node:
            if self.head == _node:
                self.head = None
                self.tail = None
                self.length = 0
            else:
                raise ValueError("node doesn't exist in the linkedlist")

        elif _node == self.head:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

        elif _node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        else:
            _node.prev.next = _node.next
            _node.next.prev = _node.prev
            self.length -= 1

    def copy(self):
        new_linked_list = DoublyLinkedList()
        for node_data in self:
            new_linked_list.insert_last(node_data)
        return new_linked_list


def test_doublylinkedlist_implementation():
    linked_list = DoublyLinkedList(1, 2, 3)

    test = "insert_last"

    linked_list.insert_last(4)
    if len(linked_list) != 4 or linked_list.tail.data != 4:
        raise Exception(f"test {test}() failed")

    linked_list.insert_last(5)
    if len(linked_list) != 5 or linked_list.tail.data != 5:
        raise Exception(f"test {test}() failed")
    print(f"### {test}() ### passed {linked_list}")
    # 1 2 3 4 5
    ##########################

    test = "insert_head"

    linked_list.insert_head(0)
    if len(linked_list) != 6 or linked_list.head.data != 0:
        raise Exception(f"test {test}() failed")
    print(f"### {test}() ### passed {linked_list}")
    # 0 1 2 3 4 5
    ########################

    test = "find_node"

    node = linked_list.find_node(3)
    if node.data != 3 or node.prev.data != 2 or node.next.data != 4:
        raise Exception(f"test {test}() failed")

    node = linked_list.find_node(0)
    if node.data != 0 or node.prev is not None or node.next.data != 1:
        raise Exception(f"test {test}() failed")
    print(f"### {test}() ### passed {linked_list}")
    # 0 1 2 3 4 5
    ########################

    test = "insert_before"

    node = linked_list.insert_before(6, 3)
    if node.data != 6 or node.prev.data != 2 or node.next.data != 3:
        print(linked_list)
        raise Exception(f"test {test}() failed")

    node = linked_list.insert_before(7, 0)
    if node.data != 7 or node.prev is not None or node.next.data != 0:
        raise Exception(f"test {test}() failed")

    print(f"### {test}() ### passed {linked_list}")
    # 7 0 1 2 6 3 4 5
    ########################

    test = "insert_after"

    node = linked_list.insert_after(8, 3)
    if node.data != 8 or node.prev.data != 3 or node.next.data != 4:
        raise Exception(f"test {test}() failed")

    node = linked_list.insert_after(9, 5)
    if (
        node.data != 9
        or node.prev.data != 5
        or node.next is not None
        or linked_list.tail != node
    ):
        raise Exception(f"test {test}() failed")

    print(f"### {test}() ### passed {linked_list}")
    # 7 0 1 2 6 3 8 4 5 9
    ########################

    test = "delete_node"

    linked_list.delete_node(node)
    if len(linked_list) != 9 or linked_list.tail.data != 5:
        raise Exception(f"test {test}() failed")

    linked_list.delete_node(linked_list.head)
    if len(linked_list) != 8 or linked_list.head.data != 0:
        raise Exception(f"test {test}() failed")

    print(f"### {test}() ### passed {linked_list}")
    # 0 1 2 6 3 8 4 5
    ########################

    test = "copy"

    new_linked_list = linked_list.copy()
    new_linked_list.delete_node(new_linked_list.tail)
    if (
        len(new_linked_list) != 7
        or new_linked_list.head.data != 0
        or new_linked_list.tail.data != 4
        or not len(linked_list) > len(new_linked_list)
    ):
        raise Exception(f"test {test}() failed")

    print(f"### {test}() ### passed {linked_list} and new list is {new_linked_list}")


if __name__ == "__main__":
    test_doublylinkedlist_implementation()
