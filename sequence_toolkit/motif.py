def find_motif(seq,motif):
	seq=seq.upper()
	motif=motif.upper()
	positions=[]

	for i in range(len(seq)-len(motif) +1):
		if seq[i:i+len(motif)]==motif:
			positions.append(i)
	return positions
