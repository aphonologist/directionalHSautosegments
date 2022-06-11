# GEN functions

# X = unlinked segment
# F = autosegment with one link
# L = leftmost link
# R = rightmost link
# M = middle link
# lowercase x, l, r reserved to code for faithfulness constraints

def gen_autoseg(input):
	candidates = set([])

	# add fully faithful candidate
	candidates.add(input)

	for i in range(len(input) - 1):
		# spread to the left
		if input[i:i+2] == 'XL':
			candidate = input[:i] + 'lM' + input[i+2:]
			candidates.add(candidate)
		if input[i:i+2] == 'XF':
			candidate = input[:i] + 'lR' + input[i+2:]
			candidates.add(candidate)
		# spread to the right
		if input[i:i+2] == 'RX':
			candidate = input[:i] + 'Mr' + input[i+2:]
			candidates.add(candidate)
		if input[i:i+2] == 'FX':
			candidate = input[:i] + 'Lr' + input[i+2:]
			candidates.add(candidate)
		# delink
		if input[i:i+2] == 'XF':
			candidate = input[:i] + 'Xx' + input[i+2:]
			candidates.add(candidate)
		if input[i:i+2] == 'FX':
			candidate = input[:i] + 'xX' + input[i+2:]
			candidates.add(candidate)
		if input[i:i+2] == 'LM':
			candidate = input[:i] + 'xL' + input[i+2:]
			candidates.add(candidate)
		if input[i:i+2] == 'MR':
			candidate = input[:i] + 'Rx' + input[i+2:]
			candidates.add(candidate)
		if input[i:i+2] == 'LR':
			candidate = input[:i] + 'xF' + input[i+2:]
			candidates.add(candidate)
			candidate = input[:i] + 'Fx' + input[i+2:]
			candidates.add(candidate)

	return sorted(list(candidates))

# parallel equivalent
#def gen_foot_parallel(input):
#	candidates = set([])
#
#	# add fully faithful candidate
#	candidates.add(input)
#
#	# build candidates of length equal to input
#	stack = ['']
#	while stack:
#		cand = stack.pop()
#		for foot in ['s', 'F', 'Tt', 'iI']:
#			cand2 = cand + foot
#			if len(cand2) == len(input):
#				candidates.add(cand2)
#			if len(cand2) < len(input):
#				stack.append(cand2)
#
#	return sorted(list(candidates))
