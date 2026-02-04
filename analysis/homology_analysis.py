
# from Bio.Blast import NCBIWWW
# from Bio import SeqIO
# record = SeqIO.read("input_sequence.fasta","fasta")
# result_handle = NCBIWWW.qblast (
#   program="blastp",
#   database="nr",
#   sequence=record.seq
# )
# with open("blast_result.xml","w")as b:
#   b.write(result_handle.read())
# print("Blast Performed Successfully!!")



from Bio.Blast import NCBIXML
with open ("blast_result.xml") as b:
  blast_record = NCBIXML.read(b)
print("Total number of hits =",(len)(blast_record.alignments))

first_alignment = blast_record.alignments[0]
first_hsp = first_alignment.hsps[0]
print("first_alignment title = ",first_alignment.title)
print("first_alignment length =",first_alignment.length)
print("first_hsp score = ",first_hsp.score)
print("first_hsp expect =",first_hsp.expect)
print("Query sequence = ",first_hsp.query)
print("Matched sequence = ",first_hsp.sbjct)
print("Alignment sequence = ",first_hsp.match)

second_alignment = blast_record.alignments[1]
second_hsp = second_alignment.hsps[0]
print("second_alignment title =",second_alignment.title)
print("second_alignment length =",second_alignment.length)
print("second_hsp score = ",second_hsp.score)
print("second_hsp expect =",second_hsp.expect)
print("Query sequence = ",second_hsp.query)
print("Matched sequence = ",second_hsp.sbjct)
print("Alignment sequence = ",second_hsp.match)


third_alignment = blast_record.alignments[2]
third_hsp = third_alignment.hsps[0]
print("third_alignment title =",third_alignment.title)
print("third_alignment length =",third_alignment.length)
print("third_hsp score = ",third_hsp.score)
print("third_hsp expect =",third_hsp.expect)
print("Query sequence = ",third_hsp.query)
print("Matched sequence = ",third_hsp.sbjct)
print("Alignment sequence = ",third_hsp.match)



