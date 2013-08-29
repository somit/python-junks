class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next
	
	def __str__(self):
		return str(self.cargo)
		

def printReverse(list):
	if list == None: return
	head = list
	tail = list.next
	printReverse(tail)
	print head
	
def run():
	head = Node();
	ptr = head;
	n = raw_input('How many nodes: ')
	n = int(n)
	for x in range(0, n):
		val = raw_input('enter number: ')
		ptr.next = Node(val)
		ptr = ptr.next
	printReverse(head.next)
	for x in range(0, n):
		print head.next
		head=head.next
		
if __name__ == "__main__":
	run()
