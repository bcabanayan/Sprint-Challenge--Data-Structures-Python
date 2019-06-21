class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # use get to determine the number of elements in self.storage
    num_elements = len(self.get())
    # if the number of elements is less than capacity...
    if num_elements < self.capacity:
      # remove the element at index num_elements
      self.storage.pop(num_elements)
      # add the element to self.storage; insert at index num_elements
      self.storage.insert(num_elements, item)
    # if the number of elements is equal to capacity...
    elif num_elements == self.capacity:
      # use self.current to keep track of number of elements added to the ringBuffer so far
      insertion_index = self.current % self.capacity
      # remove the element from the head of self.storage
      self.storage.pop(insertion_index)
      # add the new element to the tail of self.storage
      self.storage.insert(insertion_index, item)
    # keep count of elements added to ringbuffer by incrementing self.current
    self.current += 1

  def get(self):
    # start with empty array
    elements = []
    # if element exists, add to the empty array
    for element in self.storage:
      if element:
        elements.append(element)
    # return the empty array
    return elements

print(RingBuffer(4).get())
print(RingBuffer(4).append(1))