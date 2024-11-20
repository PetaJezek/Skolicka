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
        ## DORES PRIDANI PRVKU JINAK VSE V POHO 
        if self.tail == len(self.array) - 1:
            self.array[0] = n
            self.tail = 0
        else:
            self.array[self.tail + 1] = n
            self.tail += 1
    def dequeue(self):
        temp = self.array[self.head]
        self.array[self.head] = None
        return temp
    def count(self) -> int:
        none_count = 0
        for i in self.array:
            if i == None:
                none_count += 1
        return len(self.array) - none_count
    def avg(self):
        pocet = 0
        soucet = 0
        for i in self.array:
            if i == None:
                pass
            else: 
                pocet += 1
                soucet += i
        return soucet / pocet
    
q = CircularQueue(5)
q.enqueue(6)
q.enqueue(6)
q.enqueue(9)
q.enqueue(7)
q.enqueue(9)
q.enqueue(9)
q.enqueue(9)
q.enqueue(9)
q.enqueue(9)

print(q.dequeue())

        
