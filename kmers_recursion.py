def generate_kmers_rec(length):
	if length == 1:
		return ['A','T','C','G']
	else:
		result = []
		for seq in generate_kmers_rec(length-1):
			for base in ['A','T','C','G']:
				result.append(seq + base)
		return result
