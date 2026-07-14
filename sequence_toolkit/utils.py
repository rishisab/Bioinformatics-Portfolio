#fasta reader
def read_fasta(file):
    sequences = {}
    with open(file, "r") as f:
        header = ""
        seq = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if header:
                    sequences[header] = seq
                header = line[1:]
                seq = ""
            else:
                seq += line
        sequences[header] = seq
    return sequences

#sequence checker
def validate_dna(seq):
	valid_base= set("ATGC")
	seq=seq.upper()
	for base in seq:
		if base not in valid_base:
			return False
	return True

