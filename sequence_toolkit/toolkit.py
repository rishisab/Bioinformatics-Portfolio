import argparse
from utils import *
from gc_content import *
from orf import *
parser = argparse.ArgumentParser(description="Sequence Toolkit")

parser.add_argument("--input", required=True, help="Input FASTA file")
parser.add_argument("--gc", action="store_true", help="Calculate GC content")
parser.add_argument("--rev", action="store_true", help="Reverse complement")
parser.add_argument("--translate", action="store_true", help="Translate DNA")
parser.add_argument("--orf", action="store_true", help="Find ORFs")
parser.add_argument("--motif", help="Motif to search")

args = parser.parse_args()
data = read_fasta(args.input)
for name, seq in data.items():
    print("="*40)
    print(f"Sequence: {name}")

    if not validate_dna(seq):
        print("Invalid DNA sequence")
        continue

    if args.gc:
        print(f"GC Content: {gc_content(seq):.2f}%")

    if args.rev:
        print(f"Reverse Complement: {reverse_complement(seq)}")

    if args.translate:
        print(f"Protein: {transcribe_dna(seq)}")

    if args.orf:
        orfs = find_orfs(seq)
        longest = longest_orf(orfs)
        print(f"Longest ORF: {longest}")

    if args.motif:
        from motif import find_motif
        positions = find_motif(seq, args.motif)
        print(f"Motif '{args.motif}' found at: {positions}")

    print("="*40)
