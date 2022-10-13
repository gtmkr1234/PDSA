class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None
        return

    def isEmpty(self):
        if self.value is None:
            return True
        else:
            return False

    def append(self, val):
        if self.isEmpty():
            self.value = val
            return
        temp = self
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(val)
        return


if __name__ == '__main__':
