# Alex Feener: py_p4.py
import time
import multiprocessing as mp
import sys

# Given Longest Common Substring function
def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set

n_proc = sys.argv[1]
filename = sys.argv[2]

print("Number of processes:", n_proc)
print("Filename:" , filename)
id_list = []
seq_list = []
max_len = -1
max_i = 0
max_j = 0
with open(filename) as f:
	for line in f:
		s,t = line.split()
		id_list.append(s)
		seq_list.append(t)
		for i in range (len(seq_list)):
			for j in range (i+1, len(seq_list)):
				S_ = seq_list[i]
				T_ = seq_list[j]
				len_ = lcs(S_, T_)
				len_ = list(len_)
				len_ = len(len_[0])
				if len_ > max_len:
					max_len = len_
					max_i = id_list[i]
					max_j = id_list[j]
	print(max_len,  max_i, max_j)