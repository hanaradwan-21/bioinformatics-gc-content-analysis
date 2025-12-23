def read_fasta(file_path):
    sequence = ""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if not line.startswith(">"):
                    sequence += line.strip().upper()
        return sequence
    except FileNotFoundError:
        return None

def calculate_gc_content(sequence):
    """Calculates GC percentage."""
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return (g_count + c_count) / len(sequence) * 100

def get_reverse_complement(sequence):
    """Generates reverse complement."""
    complement_map = str.maketrans("ATCG", "TAGC")
    return sequence.translate(complement_map)[::-1]

def transcribe(sequence):
    """DNA to RNA."""
    return sequence.replace('T', 'U')

def translate_rna(rna_sequence):
    """RNA to Protein."""
    codon_table = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y',
        'UAC': 'Y', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'UAA': '_',
        'UAG': '_', 'UGA': '_', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L',
        'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R',
        'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I',
        'AUA': 'I', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S',
        'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V',
        'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A',
        'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    protein = ""
    for i in range(0, len(rna_sequence) - 2, 3):
        codon = rna_sequence[i:i+3]
        protein += codon_table.get(codon, '?')
    return protein