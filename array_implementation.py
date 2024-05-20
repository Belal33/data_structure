import ctypes


class MyArray:

    @classmethod
    def resize(cls, source: ctypes.POINTER(ctypes.c_int), newSize: int):  # type: ignore
        # Check if newSize is valid
        if newSize <= 0 or source is None:
            return

        # Allocate a new array of size newSize
        newArray = (ctypes.c_int * newSize)()

        # Copy the contents of the old array into the new array
        ctypes.memmove(
            newArray,
            source.contents,
            ctypes.sizeof(ctypes.c_int) * len(source.contents),
        )

        # Update the reference to the source array with the new array
        source.contents = newArray
        # print(list(source.contents))
        print(list(newArray))


if __name__ == "__main__":
    sourceArr = (ctypes.c_int * 3)(4654, 921, 762)
    print(len(sourceArr))
    sourceArrPointer = ctypes.pointer(sourceArr)
    MyArray.resize(sourceArrPointer, 7)

    print(list(sourceArrPointer.contents))
    print(list(sourceArr))
