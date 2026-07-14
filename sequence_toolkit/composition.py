def nucleotide_composition(seq):
	seq=seq.upper()
	return {
		"A":seq.count("A"),
		"T":seq.count("T"),
		"G":seq.count("G"),
		"C":seq.count("C") }

def sequence_stats(seq):
	return {
		"length":len(seq),
		"gc_count":seq.count("G")+seq.count("C"),
		"at_count":seq.count("A")+seq.count("T")
		}
