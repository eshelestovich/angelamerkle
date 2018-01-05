import sys
import hashlib
import time
import functools

class Node:

	def do_hash(self, input):
		if not input:
			return '' 
		return hashlib.sha256(hashlib.sha256(input.encode('utf-8')).hexdigest().encode('utf-8')).hexdigest()

	def compute_hash(self):
		leftDigest = str(self.left.digest) if self.left != None else ''
		rightDigest = str(self.right.digest) if self.right != None else ''
		self.digest = self.do_hash(leftDigest + rightDigest)

	def __init__(self, left = None, right = None, parent = None, value = ''):
		self.parent = parent
		self.digest = self.do_hash(value)

		if left != None:
			left.parent = self
		self.left = left

		if right != None:
			right.parent = self
		self.right = right

	def __str__(self):
		return 'node [' + str(self.digest) + ']'
