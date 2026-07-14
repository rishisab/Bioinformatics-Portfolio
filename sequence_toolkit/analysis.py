from utils import read_fasta, validate_dna
from composition import nucleotide_composition, sequence_stats
from motif import find_motif

data = read_fasta("examples/sample.fasta")

for name, seq in data.items():
    print("="*40)
    print(f"Sequence: {name}")

    if not validate_dna(seq):
        print("Invalid DNA sequence")
        continue

    stats = sequence_stats(seq)
    print(f"Length: {stats['length']}")

    comp = nucleotide_composition(seq)
    print(f"A:{comp['A']} T:{comp['T']} G:{comp['G']} C:{comp['C']}")

    motif_positions = find_motif(seq, "ATG")
    print(f"ATG positions: {motif_positions}")

    print("="*40)
