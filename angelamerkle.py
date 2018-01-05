import sys
import hashlib
import time
import functools
from mnode import Node

class AngelaMerkle:

	def group_in_pairs(self, items):
		# duplicate last element if length is odd
		if len(items) % 2 != 0:
			items.append(items[len(items) - 1])
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
			node = Node(left, right)
			node.compute_hash()
			nodes.append(node)
		
		# recursively call to produce the next upper layer
		return self.build_layer(nodes)

	def build_tree(self):
		if self.sourceList == None or len(self.sourceList) == 0:
			return
		# build first layer (leafs) with hashes
		firstLayer = [Node(value = s) for s in self.sourceList]
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

