class CircularQueue():
    def __init__(self, size):
        self.array = size * [None]
        self.head = size//2
        self.tail = self.head
    def resize(self):
        array = [None] * len(self.array) * 2
        print(f"Resized to len(array) elements")
        if self.head > self.tail:
            for i in range(self.head, len(self.array)-1):
                array[i-self.head] = self.array[i]
            for i in range(self.tail):
                array[i+len(self.array)-self.head] = self.array[i]
            self.head = 0
            self.tail = len(self.array) - 1
            self.array = array    
        if self.head < self.tail:
            for i in range(self.tail):
                array[i] = self.array[i]
            self.array = array
        else: 
            array[0] = self.array[0]
            self.array = array
    def checkIfFull(self):
        if self.head > self.tail:
            if self.head - self.tail == 1:
                return True
        elif self.head < self.tail and self.head == 0:
            return True
        elif self.head == self.tail and len(self.array) == 1:
            return True
        else:
            return False
    def enqueue(self, n: int):
        if self.checkIfFull():
            self.resize()
        self.array[self.tail + 1] = n
    def dequeue(self):
        temp = self.array[self.head]
        self.array[self.head] = None
        return temp
     