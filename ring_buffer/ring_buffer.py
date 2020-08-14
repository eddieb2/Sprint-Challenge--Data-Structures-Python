class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.data = []

    def append(self, item):
        # The append method adds the given element to the buffer.

        # if data is not full, append data to the list
        if len(self.data) < self.capacity:
            self.data.append(item)

        # if data is full, replace oldest value with new value
        if len(self.data) == self.capacity:
            self.data[self.index] = item

        # sets the self.index to the index of the oldest value
        # next index or oldest value = cur index + 1 % max capacity
        self.index = (self.index + 1) % self.capacity

    def get(self):
        # The get method returns all of the elements in the buffer
        # in a list in their given order. It should not return any None values
        # in the list even if they are present in the ring buffer.
        return self.data


rb1 = RingBuffer(3)

print(f'{rb1.data}') # []
rb1.append(1)
rb1.append(2)
rb1.append(3)
print(f'{rb1.data}') # [1,2,3]
rb1.append(4)
print(f'{rb1.data}') # [4,2,3]
rb1.append(5)
print(f'{rb1.data}') # [4,5,3]
rb1.append(6)
print(f'{rb1.data}') # [4,5,6]
