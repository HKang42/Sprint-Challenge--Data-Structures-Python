class RingBuffer:
    def __init__(self, capacity, values = [], oldest = 0):
        self.capacity = capacity
        self.values = values
        self.oldest = oldest

    def append(self, item):
        #self.values.insert(0,item)
        if len(self.values) < self.capacity:
            self.values.append(item)
            self.oldest = 0
        
        # while number of elements is at capacity
        elif len(self.values) == self.capacity:
            
            self.values[self.oldest] = item
            self.oldest += 1

            if self.oldest >= self.capacity:
                self.oldest = 0
            """
            self.values.pop(0)
            print("HI", self.values)
            self.values.append(item)
            """

    def get(self):
        return self.values


# q = RingBuffer(5)
# q.append("A")
# print(q.get())