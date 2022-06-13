## Constraints
# Direction L/R -> directional evaluation
# Direction N   -> traditional evaluation

# *F
# penalizes leftmost/rightmost segment linked to autosegment
class F:
	def __init__(self, direction):
		self.direction = direction
		self.name = '*F'
		if direction != 'N':
			self.name += direction

	def vios(self, candidate):
		candidate = candidate.upper()
		loci = [0] * len(candidate)
		if self.direction == 'L':
			for i in range(len(candidate)):
				if candidate[i] in ['F', 'R']:
					loci[i] = 1
		if self.direction == 'R':
			candidate = candidate[::-1]
			for i in range(len(candidate)):
				if candidate[i] in ['F', 'L']:
					loci[i] = 1

		if self.direction == 'N': return [sum(loci)]
		return loci

# AlignL
# one vio for every segment that seperates leftmost segment from left edge
class AlignL:
	def __init__(self):
		self.name = 'AlignL'

	def vios(self, candidate):
		loci = [0]
		for i in range(len(candidate)):
			if candidate[i] in ['F', 'L']:
				loci[0] += i
		return loci

# AlignR
# one vio for every segment that seperates rightmost segment from right edge
class AlignR:
	def __init__(self):
		self.name = 'AlignR'

	def vios(self, candidate):
		loci = [0]
		for i in range(len(candidate)):
			if candidate[i] in ['F', 'R']:
				loci[0] += len(candidate) - 1 - i
		return loci

### Faithfulness constraints are binary

# Dep(link)
# don't insert autosegmental links
class DepLink:
	def __init__(self):
		self.name = 'DEP(link)'

	def vios(self, candidate):
		if 'l' in candidate or 'r' in candidate:
			return [1]
		return [0]

# Max(link)
# don't delete autosegmental links
class MaxLink:
	def __init__(self):
		self.name = 'MAX(link)'

	def vios(self, candidate):
		if 'x' in candidate:
			return [1]
		return [0]
