class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    pass

  def get(self):
    elements = []
    for element in self.storage:
      if element:
        elements.append(element)
    return elements

print(RingBuffer(4).get())