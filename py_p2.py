# Alex Feener: py_p2.py
import sys
filename = sys.argv[1]
with open(filename) as f:
	for line in f:
		line = line.lower().split()
		seq_id = line[0]
		dna = line[1]
		for i in range(len(dna)):
			if dna[i:i+3] == 'atg' or dna[i:i+3] == 'gtg':
				for j in range (i+3, len(dna), 3):
					if dna[j:j+3] == 'tag':
						length = j - i + 3
						if length % 3 == 0:
							if length > 32 and length <= 99:
								print(seq_id,  i,  length,  dna[i:i+3],  dna[j:j+3])
							break