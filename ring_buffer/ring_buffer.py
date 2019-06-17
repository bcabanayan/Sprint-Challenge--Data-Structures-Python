class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    

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