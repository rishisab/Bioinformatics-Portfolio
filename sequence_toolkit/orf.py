def find_orfs(seq):
    seq = seq.upper()
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []

    for frame in range(3):
        for i in range(frame, len(seq) - 2, 3):
            codon = seq[i:i+3]

            if codon == "ATG":
                for j in range(i, len(seq) - 2, 3):
                    stop_codon = seq[j:j+3]

                    if stop_codon in stop_codons:
                        orf = seq[i:j+3]
                        orfs.append(orf)
                        break

    return orfs


def longest_orf(orfs):
    if not orfs:
        return None
    return max(orfs, key=len)
