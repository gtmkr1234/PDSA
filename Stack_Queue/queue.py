class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def addq(self,v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isEmpty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v

    def __str__(self):
        return str(self.queue)


