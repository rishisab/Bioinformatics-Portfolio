def gc_content(seq):
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100
def reverse_complement(seq):
    complement = {
        "A": "T", "T": "A",
        "G": "C", "C": "G"
    }
    return "".join(complement[base] for base in reversed(seq.upper()))
def transcribe_dna(seq):
    return seq.upper().replace("T", "U")
