class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.data = []

    def append(self, item):
        # The append method adds the given element to the buffer.
        # if data is not full, append data to the list
        if self.data < self.capacity:
            pass

        # if data is full, replace oldest value with new value
        if self.data == self.capacity:
            pass

    def get(self):
        # The get method returns all of the elements in the buffer
        # in a list in their given order. It should not return any None values
        # in the list even if they are present in the ring buffer.
        pass