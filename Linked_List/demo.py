class Node:
  def __init__(self, val, next_node=None):
    self.val = val
    self.next_node = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def traverse_list(self):
    current_val = self.head
    while current_val:
      print(current_val)
      current_val = current_val.next_node
    
if __name__ == "__main__":
  linked_list = LinkedList()
  
