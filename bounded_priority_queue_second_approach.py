class BoundedPriorityQueue:
    def __init__(self ,max_priority):
        self._queue = list()
        self._max_priority = max_priority

#-------------------------------------------------------------------------------------------------------------------------

    def __len__(self):
        return len(self._queue)
    
#-------------------------------------------------------------------------------------------------------------------------

    def is_empty(self):
        return len(self) == 0
    
#-------------------------------------------------------------------------------------------------------------------------

    def enqueue(self ,tpl_item):
        assert 0 <= tpl_item[1] <= self._max_priority ,"Priority out of range."
        if self.is_empty():
            self._queue.append(tpl_item)

        else:
            inserted = False
            for idx in range(len(self)):
                if self._queue[idx][1] > tpl_item[1]:
                    self._queue.insert(idx ,tpl_item)
                    inserted = True
                    break
            
            if not inserted:
                self._queue.append(tpl_item)

#-------------------------------------------------------------------------------------------------------------------------

    def dequeue(self):
        assert not self.is_empty() ,"Cannot remove from empty queue."
        return self._queue.pop(0)

#=========================================================================================================================

queue = BoundedPriorityQueue(max_priority=10)

# Enqueue items
queue.enqueue(('Task 1', 5))
queue.enqueue(('Task 2', 3))
queue.enqueue(('Task 3', 8))
queue.enqueue(('Task 4', 1))

print("Queue after enqueues:")
print(queue._queue)  # Should show items in order of their priority


# Dequeue items
print("\nDequeue operations:")
print(queue.dequeue())  # Should remove ('Task 4', 1)
print(queue.dequeue())  # Should remove ('Task 2', 3)
print(queue.dequeue())  # Should remove ('Task 1', 5)
print(queue.dequeue())  # Should remove ('Task 3', 8)

print("\nIs the queue empty?")
print(queue.is_empty())