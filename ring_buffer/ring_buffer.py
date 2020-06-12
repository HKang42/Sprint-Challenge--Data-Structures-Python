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


"""
for some reason, the test doesn't execute from top to bottom.

This is causing it to fail the first test in the test code.

First test is supposed to be inserting a single element. I have reproduced the test above where it works.

What's the problem?
In the test file, the "first" test isn't being executed first (i.e. tests are not being run from top to bottom). 
This is a problem because the tests don't re-initialize the RingBuffer object.
So the buffer isn't cleared when the test code checks to see if you can create a 1 element list

See print statements in the test_ring_buffer.py file.


"""