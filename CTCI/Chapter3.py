"""
Chapter 3 - Stacks and Queues
Aman Singh


Key concepts: Stacks, Queues
"""


# Q1: Three in One

"""
You could use a single array to implement three stacks by 

METHOD 1:
"""


# Q2: Stack Min


"""
In order to have a stack have a function min which returns teh minimum element,
we want to make sure that each node has access to the minimum to each substack.
As such, we might define a stack node with 2 values: the node value and the min 
of the substack up to that node
"""

# Q3: Stack of Plates


class Node(object):

	def __init__(self, value):
		self.value = value
		self.above = None
		self.below = None


class Stack(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.top = None
		self.bottom = None

	def is_full(self):
		return self.size == self.capacity

	def is_empty(self):
		return self.size == self.capacity

	def join(self, above, below):
		if below:
			below.above = above
		if above:
			above.below = below

	def push(self, v):
		if self.size >= self.capacity:
			return False
		self.size += 1
		n = Node(v)
		if self.size == 1:
			self.bottom = n
		self.join(n, self.top)
		self.top = n
		return True

	def pop(self):
		if not self.top:
			return None
		t = self.top
		self.top = self.top.below
		self.size -= 1
		return t.value

	def remove_bottom(self):
		b = self.bottom
		self.bottom = self.bottom.above
		if self.bottom:
			self.bottom.below = None
		self.size -= 1
		return b.value

	def peek(self):
		return self.top.value


class SetofStacks(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.stacks = []

	def get_last_stack(self):
		if not self.stacks:
			return None
		return self.stacks[-1]

	def is_empty(self):
		last = self.get_last_stack()
		return not last or last.is_empty()

