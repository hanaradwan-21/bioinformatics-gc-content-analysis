import pandas as pd
from dna_utils import read_fasta, get_reverse_complement, transcribe, translate_rna, calculate_gc_content

# List of files to analyze
files = {
    "Human": "data/human.fasta.fasta",
    "Bacteria": "data/bacteria.fasta.fasta",
    "Virus": "data/virus.fasta.fasta"
}

results_list = []

print("Analyzing sequences and saving results to Excel...")

for species, path in files.items():
    dna_seq = read_fasta(path)
    if dna_seq:
        gc = calculate_gc_content(dna_seq)
        rna_seq = transcribe(dna_seq)
        protein_seq = translate_rna(rna_seq)
        rev_comp = get_reverse_complement(dna_seq)

        # Append results properly with clear column names
        results_list.append({
            "Species": species,
            "GC Content (%)": round(gc, 2),
            "DNA Sequence": dna_seq,
            "Reverse Complement": rev_comp,
            "RNA Sequence": rna_seq,
            "Protein Sequence": protein_seq
        })

# Create Excel file with clean columns
df = pd.DataFrame(results_list)
df.to_excel("DNA_Analysis_Results.xlsx", index=False)

print("DNA_Analysis_Results.xlsx has been created successfully!")