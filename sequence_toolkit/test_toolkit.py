from utils import read_fasta, validate_dna
from gc_content import gc_content
from reverse_complement import reverse_complement
from dna_transcribe import translate_dna
from translate_orf import translate_orf_all_frames
from orf import find_orfs, longest_orf
import argparse

data = read_fasta("examples/sample.fasta")

for name, seq in data.items():
    print(f"Sequence: {name}")

    if not validate_dna(seq):
        print("Invalid dna seq")
        continue

    print(f"GC Content: {gc_content(seq):.2f}%")
    print(f"Reverse Complement: {reverse_complement(seq)}")
    print(f"Protein: {translate_dna(seq)}")

    print(f"ORF Protein: {translate_orf_all_frames(seq)}")


    orfs = find_orfs(seq)

    print(f"Longest ORF: {longest_orf(orfs)}")

    longest = longest_orf(orfs)
    if longest:
        print(f"Longest ORF (DNA): {longest}")
        print(f"Longest ORF (Protein): {translate_dna(longest)}")
    print("-"*30)
