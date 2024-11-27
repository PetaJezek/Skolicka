class CircularQueue():
    def __init__(self, size):
        self.array = size * [None]
        self.head = 0
        self.tail = self.head
        self.pocet = 0
    def resize(self):
        new_size = len(self.array) * 2
        new_array = [None] * new_size
        print(f"Resized to {new_size} elements")
        for i in range(self.pocet):
            new_array[i] = self.array[(self.head + i) % len(self.array)]
        self.array = new_array
        self.head = 0
        self.tail = self.pocet - 1
    def checkIfFull(self):
        return (self.tail + 1) % len(self.array) == self.head
    def enqueue(self, n: int):
        self.pocet += 1
        if self.array.count(None) == len(self.array):
            self.array[self.head] = n
        else:
            if self.tail == len(self.array) - 1:
                self.array[0] = n
                self.tail = 0
            else:
                self.array[self.tail + 1] = n
                self.tail += 1
        if self.checkIfFull():
            self.resize()
    def dequeue(self):
        self.pocet -= 1
        temp = self.array[self.head]
        self.array[self.head] = None
        if self.head == len(self.array)-1:
            self.head = 0
        else:
            self.head += 1
        return temp
    def count(self) -> int:
        return self.pocet
    def avg(self): 
        soucet = 0
        for i in range(self.pocet):
                soucet += self.array[(self.head + i) % len(self.array)]
        return soucet / self.pocet
    
