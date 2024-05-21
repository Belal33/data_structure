from my_linkedlist_implementation import LinkedList


class Stack:
    def __init__(self, unique: bool = False):
        self.__data_list = LinkedList(unique_data=unique)

    def push(self, data):
        return self.__data_list.insert_head(data)

    def pop(self):
        return self.__data_list.delete_head()

    def peek(self):
        return self.__data_list.head.data

    def is_empty(self):
        return self.__data_list.head is None

    def __repr__(self):
        return self.__data_list.__repr__()


if __name__ == "__main__":
    s = Stack(True)
    s.push(1)
    s.push(2)
    s.push(5)
    s.push(3)

    print(s.pop())
    print(s.pop())
    print(s.is_empty())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())
