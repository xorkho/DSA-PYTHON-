class _PriorityQEntry( object ):
  def __init__( self, item, priority ):
    self.item = item
    self.priority = priority

class PriorityQueue :

  # Create an empty unbounded priority queue.
  def __init__( self ):
    self._qList = list()

  # Returns True if the queue is empty.
  def isEmpty(self):
    return len(self._qList) == 0

  # Returns the number of items in the queue.
  # Adds the given item to the queue.
  def enqueue( self, item, priority ):
    # Create a new instance of the storage class and append it to the list.
    entry = _PriorityQEntry( item, priority )
    self._qList.append( entry )

  def dequeue(self):
    assert not self.isEmpty(), "Cannot dequeue from an empty queue."

    # Initialize the highest priority and its index
    highest_index = 0
    highest_priority = self._qList[0].priority

    # Iterate through the list to find the entry with the highest priority
    for i in range(1, self.len()):  # Start from the second element
        if self._qList[i].priority < highest_priority:  # Smaller number means higher priority
            highest_priority = self._qList[i].priority
            highest_index = i

    # Remove the entry with the highest priority and return the item
    entry = self._qList.pop(highest_index)
    return entry.item


  def len( self ):
     return len(self._qList)

  def __str__(self):
    # Create a list of tuples (item, priority) for representation
    return ', '.join(f'({entry.item}, {entry.priority})' for entry in self._qList)


Q = PriorityQueue()
Q.enqueue("purple",5)
Q.enqueue("black",1)
Q.enqueue("orange",3)
Q.enqueue("white",0)
Q.enqueue("green",1)
Q.enqueue("yellow",5)
print(Q)
Q.dequeue()
print(Q)