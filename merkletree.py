import sys
import mmh3
import time
import functools

class Node:

	def compute_hash(self, seed = 0):
		leftDigest = str(self.left.digest) if self.left != None else ''
		rightDigest = str(self.right.digest) if self.right != None else ''
		self.digest = mmh3.hash128(leftDigest + rightDigest, seed)

	def __init__(self, digest = 0, left = None, right = None, parent = None):
		self.parent = parent
		self.digest = digest

		if left != None:
			left.parent = self
		self.left = left

		if right != None:
			right.parent = self
		self.right = right

	def __str__(self):
		return 'node [' + str(self.digest) + ']'


class AngelaMerkle:

	def group_in_pairs(self, items):
		if len(items) % 2 != 0:
			items.append(None)
		pairs = list(zip(items[::2], items[1::2]))
		return pairs

	def build_layer(self, layer):
		# until only the root left
		if len(layer) == 1:
			return layer
		# current layer of nodes
		nodes = []
		for pair in self.group_in_pairs(layer):
			left, right = pair[0], pair[1]
			node = Node(0, left, right)
			node.compute_hash() # can be seeded with int(time.time())
			nodes.append(node)
		# recursively call to produce the next upper layer
		return self.build_layer(nodes)

	def build_tree(self):
		if self.sourceList == None or len(self.sourceList) == 0:
			return
		# init first layer (leafs) with hashes
		firstLayer = [Node(mmh3.hash128(s)) for s in self.sourceList]
		self.root = self.build_layer(firstLayer)[0]

	def __init__(self, sourceList):
		self.sourceList = sourceList
		self.root = 0
		self.build_tree()

	def __str__(self):
		return str(self.root)

def main(args):
	print('enter a key set to build a tree from: ', end = '')
	strings = [x for x in input().split()]
	tree = AngelaMerkle(strings)
	print(tree)

if __name__ == '__main__':
	main(sys.argv)


