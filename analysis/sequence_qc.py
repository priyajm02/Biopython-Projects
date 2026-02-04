from Bio import SeqIO
from collections import Counter
record = SeqIO.read("input_sequence.fasta", "fasta")
seq = str(record.seq)
print("Sequence ID:", record.id)
print("Sequence Description:", record.description)
print("Sequence length:", len(record))

aa_count = Counter(seq)
print("Amino acid composition:")
for aa, count in aa_count.items():
    print(f"{aa}: {count}")