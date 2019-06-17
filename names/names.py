import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
        
# implementing solution with linked list

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_next(self):
        return self.next
  
    def set_next(self, node):
        self.next = node

class LinkedList:
  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail
  
  def add_to_tail(self, value):
    new_tail = Node(value)
    # point existing tail to new tail
    if self.tail:
        self.tail.set_next(new_tail)
    # don't need to repoint new tail, already pointing to None
    self.tail = new_tail

print(LinkedList(None, None).add_to_tail(1))

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

