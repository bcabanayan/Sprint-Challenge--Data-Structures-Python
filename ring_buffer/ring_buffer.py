class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # use get to determine the number of elements in self.storage
    # if the number of elements is less than capacity...
      # add the element to self.storage; number of elements = index to be inserted into
    # if the number of elements is equal to capacity...
      # remove the element from the head of self.storage
      # add the new element to the tail of self.storage


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