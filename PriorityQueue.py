from SinglyLinkedList import SinglyLinkedList

class PriorityNode:
	priority = -1
	value = ''
	def __init__(self, value, priority):
		self.priority = priority
		self.value = value

	def getValue(self):
		return self.value
	def getPriority(self):
		return self.priority

class PriorityQueue:
	list = ''

	def __init__(self):
		self.list = SinglyLinkedList()

	def enqueueWithPriority(self, value, priority):
		idxInsert = 0
		for itr in range(self.list.getSize()):
			node = self.list.get(itr)
			if node.getValue() == '':
				idxInsert = itr
				break
			if node.getValue().getPriority() < priority:
				idxInsert = itr
				break
			else:
				idxInsert = itr + 1
		self.list.insertAt(PriorityNode(value, priority), idxInsert)

	def dequeueWithPriority(self):
		return self.list.removeAt(0).getValue()

if __name__ == '__main__':
	pq = PriorityQueue()
	pq.enqueueWithPriority('ABC', 1)
	pq.enqueueWithPriority('BCD', 2)
	pq.enqueueWithPriority('CDE', 3)
	pq.enqueueWithPriority('DEF', 99)

	print(pq.dequeueWithPriority())
	print(pq.dequeueWithPriority())
	print(pq.dequeueWithPriority())
	print(pq.dequeueWithPriority())
		
	