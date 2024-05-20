class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next: LinkedListNode = None

    def __repr__(self) -> str:
        return str(f"node_data = {self.data}")


class LinkedListIterator:
    def __init__(self, _node: LinkedListNode):
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


class LinkedList:
    iter_class = LinkedListIterator
    node_class = LinkedListNode

    def __init__(self, *args):

        self.head: LinkedList.node_class = None
        self.tail: LinkedList.node_class = None
        self.length = 0
        if len(args):
            print("args:" + str(args))
            for data in args:
                self.insert_last(data)
            self.length = len(args)
        self.itr_obj = self.iter_class(self.head)

    def __iter__(self):
        self.itr_obj = self.iter_class(self.head)
        return self.itr_obj

    def __repr__(self) -> str:
        linked_list_repr = ""
        for node_data in self:
            linked_list_repr += f"({node_data}) "
        return f"linked_list -{(str(self.length))}-> |{self.head and self.head.data}| {linked_list_repr} |{self.tail and self.tail.data}|"

    @property
    def next_node(self):
        itr_obj = self.itr_obj
        return itr_obj.current() or self.head

    def find_node(self, _data_to_find):
        # check if the list is empty
        if self.head is None:
            return None

        current_node = self.head
        for node_data in self:
            if _data_to_find == node_data:
                return current_node
            current_node = self.next_node
        return None

    def insert_last(self, _data):
        new_node = self.node_class(_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return new_node

    def insert_after(self, _data_to_insert, _data_to_find):
        # search about the node contian _data_to_find return error if not found it
        ref_node: LinkedListNode = self.find_node(_data_to_find)
        if ref_node is None:
            raise ValueError(f"list doesn't contain this value '{_data_to_find}'")

        # make new_node contain _data_to_insert
        new_node = self.node_class(_data_to_insert)
        # make new_node.next be the reference_node.next
        new_node.next = ref_node.next
        # check if ref_node is the tail
        if new_node.next is None:
            self.tail = new_node
        # make reference_node.next be the new_node
        ref_node.next = new_node
        # increase the list length
        self.length += 1
        return new_node

    def insert_before(self, _data_to_insert, _data_to_find):
        # search about the node contian _data_to_find return error if not found it
        # create new_node contain _data_to_insert
        # make new_node.next be the ref_node
        # check if ref_node was the head make new_node be the head
        # find previous_node
        # make previous_node.next be the new_node
        # increase the list length
        ref_node: LinkedListNode = self.find_node(_data_to_find)
        if ref_node is None:
            raise ValueError(f"list doesn't contain this value '{_data_to_find}'")

        new_node = self.node_class(_data_to_insert)
        new_node.next = ref_node
        if self.head == ref_node:
            self.head = new_node
        else:
            previous_node = self.get_previous_node(ref_node)
            if previous_node is not None:
                previous_node.next = new_node
        self.length += 1
        return new_node

    def get_previous_node(self, _node: LinkedListNode):
        # validate that _node is not None
        # check if the list is empty raise an error
        # check if _node is the head then return None
        # loop through the list
        # return the node if the node.next is _node
        # if node doesn't exist raise an error
        if _node is None:
            raise ValueError(f"node can't be None")
        if self.head is None:
            raise ValueError(f"the node doesn't exist in the linkedlist")
        if self.head == _node:
            return None
        current_node = self.head
        for _ in self:
            if current_node.next is _node:
                return current_node
            current_node = self.next_node
        raise ValueError(f"the node doesn't exist in the linkedlist{_node}")

    def delete_tail(self):
        if self.tail is None:
            raise ValueError(f"the linked list is empty")
        new_tail = self.get_previous_node(self.tail)
        if new_tail is None:
            self.head = None
            self.tail = None
        else:
            new_tail.next = None
            self.tail = new_tail
        self.length -= 1

    def delete_head(self):
        if self.head is None:
            raise ValueError(f"the linked list is empty")
        old_head = self.head
        self.head = old_head.next

        del old_head
        self.length -= 1

    def delete_node(self, _node: LinkedListNode):
        if self.head is None:
            raise ValueError(f"the linked list is empty")
        if self.head == _node:
            self.delete_head()
        elif self.tail == _node:
            self.delete_tail()
        else:
            self.get_previous_node(_node).next = _node.next
            del _node


def test_linked_list_structure_and_operations():
    passed_test_cases = []
    failed_test_cases = []
    linked_list = LinkedList()
    # test insert_last
    test_1 = "test insert_last"
    node_1 = linked_list.insert_last(1)
    node_2 = linked_list.insert_last(2)
    node_3 = linked_list.insert_last(3)

    print(test_1)
    if node_1.data == 1 and node_2.data == 2 and node_3.data == 3:
        for data, i in zip(linked_list, [1, 2, 3]):
            if data != i:
                failed_test_cases.append(test_1)
                break
        passed_test_cases.append(test_1)
    print(f"{linked_list } = 1 2 3 ")
    # 1 2 3
    ########################

    # test insert_after
    test_2 = "test insert_after"
    node_4 = linked_list.insert_after(4, 3)

    print(test_2)
    if node_4.data == 4:
        for data, i in zip(linked_list, [1, 2, 3, 4]):
            if data != i:
                failed_test_cases.append(test_2)
                break
        passed_test_cases.append(test_2)
    print(f"{linked_list } = 1 2 3 4")
    # 1 2 3 4
    ###############
    # test insert_before
    test_3 = "test insert_before"
    node_0 = linked_list.insert_before(0, 1)

    print(test_3)
    if node_0.data == 0:
        for data, i in zip(linked_list, [0, 1, 2, 3, 4]):
            if data != i:
                failed_test_cases.append(test_3)
                break
        passed_test_cases.append(test_3)
    print(f"{linked_list } = 0 1 2 3 4")
    # 0 1 2 3 4

    ###############

    # test find_node
    test_4 = "test find_node"

    print(test_4)
    if linked_list.find_node(3) and linked_list.find_node(3).data == 3:
        for data, i in zip(linked_list, [0, 1, 2, 3, 4]):
            if data != i:
                failed_test_cases.append(test_4)
                break
        passed_test_cases.append(test_4)

    print(f"{linked_list } = 0 1 2 3 4")

    # 0 1 2 3 4
    ###############

    # test delete_node
    test_5 = "test delete_node"
    linked_list.delete_node(node_4)
    print(test_5)
    if linked_list.find_node(4) is None:
        for data, i in zip(linked_list, [0, 1, 2, 3]):
            if data != i:
                failed_test_cases.append(test_5)
                break
        passed_test_cases.append(test_5)

    print(f"{linked_list } = 0 1 2 3 ")
    # 0 1 2 3

    ###############

    # test delete_tail
    test_6 = "test delete_tail"
    linked_list.delete_tail()
    print(test_6)
    if linked_list.find_node(3) is None:
        for data, i in zip(linked_list, [0, 1, 2]):
            if data != i:
                failed_test_cases.append(test_6)
                break
        passed_test_cases.append(test_6)

    print(f"{linked_list } = 0 1 2 ")
    # 0 1 2

    ###############

    # test delete_head
    test_7 = "test delete_head"
    linked_list.delete_head()
    print(test_7)
    if linked_list.find_node(0) is None:
        for data, i in zip(linked_list, [1, 2]):
            if data != i:
                failed_test_cases.append(test_7)
                break
        passed_test_cases.append(test_7)

    print(f"{linked_list } = 1 2 ")
    # 1 2

    return passed_test_cases, failed_test_cases


if __name__ == "__main__":
    passed, failed = test_linked_list_structure_and_operations()
    print("\n")
    print(f"failed: {failed}")
    print("\n")
    print(f"passed: {len(passed)}")
    print("\n")
