class CircularQueue():
    def __init__(self, size):
        self.array = size * [None]
        self.head = size//2
        self.tail = self.head
    def resize(self):
        array = [None] * len(self.array) * 2
        print(f"Resized to " +  str(len(array)) + " elements")
        if self.head > self.tail:
            for i in range(self.head, len(self.array)):
                array[i-self.head] = self.array[i]
            for i in range(self.tail+1):
                array[i+len(self.array)-self.head] = self.array[i]
            self.head = 0
            self.tail = len(self.array) - 1
            self.array = array    
        elif self.head < self.tail:
            for i in range(self.tail+1):
                array[i] = self.array[i]
            self.array = array
        else: 
            array[0] = self.array[0]
            self.array = array
    def checkIfFull(self):
        if (self.array).count(None) == 0:
            if self.head > self.tail:
                if self.head - self.tail == 1:
                    return True
            elif self.head < self.tail and self.head + self.tail == len(self.array)-1:
                return True
            elif self.head == self.tail:
                return True
        else:
            return False
    def enqueue(self, n: int):
        ## DORES PRIDANI PRVKU JINAK VSE V POHO 
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
        temp = self.array[self.head]
        self.array[self.head] = None
        if self.head == len(self.array)-1:
            self.head = 0
        else:
            self.head += 1
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
    

