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
    if self.head is None:
        self.head = new_tail
    if self.tail:
        self.tail.set_next(new_tail)
    self.tail = new_tail

def remove_dupes(name_list):
    start_node = name_list.head
    # TEST CODE TO PRINT EVERY VALUE IN LINKED LIST
    # while start_node.next:
    #     print(start_node.value)
    #     start_node = start_node.next
    # TEST CODE ENDS HERE
    start_next = start_node.next
    name_store = set([start_node.value])
    while start_next:
        value = start_next.value
        if value in name_store:
            start_node.next = start_next.next
            start_next = start_next.next
        else:
            name_store.add(value)
            start_node = start_next
            start_next = start_next.next

def printDupes(name_list):
    start_node = name_list.head
    # TEST CODE TO PRINT EVERY VALUE IN LINKED LIST
    # while start_node.next:
    #     print(start_node.value)
    #     start_node = start_node.next
    # TEST CODE ENDS HERE
    start_next = start_node.next
    name_store = set([start_node.value])
    while start_next:
        value = start_next.value
        if value in name_store:
            duplicates.append(value)
            start_next = start_next.next
        else:
            name_store.add(value)
            start_next = start_next.next

name_list1 = LinkedList(None, None)
name_list2 = LinkedList(None, None)

for name_1 in names_1:
    name_list1.add_to_tail(name_1)

for name_2 in names_2:
    name_list2.add_to_tail(name_2)

remove_dupes(name_list1)
remove_dupes(name_list2)

names1_without_dupes = []
names2_without_dupes = []

starting_node1 = name_list1.head
while starting_node1:
    names1_without_dupes.append(starting_node1.value)
    starting_node1 = starting_node1.next

starting_node2 = name_list2.head
while starting_node2:
    names2_without_dupes.append(starting_node2.value)
    starting_node2 = starting_node2.next

combined_list = LinkedList(None, None)

for name_1 in names1_without_dupes:
    combined_list.add_to_tail(name_1)

for name_2 in names2_without_dupes:
    combined_list.add_to_tail(name_2)

printDupes(combined_list)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

