# Biopython-Project
This Study tries to predict the function of a protein whose function is not known yet, by analyzing its sequence and comparing it with similar known proteins.

# In-Silico Functional characterization of the uncharacterized protein (LOC728138) using Sequence and Homology-based Analysis.

## Project Description
This project aims to perform functional annotation of an uncharacterized protein from Homo sapiens using bioinformatics tools. The protein sequence was analyzed using homology-based methods, conserved domain analysis, and Gene Ontology annotation to predict its possible function.

The selected protein is LOC728138 (UniProt ID: B2RXJ9), which is an uncharacterized protein of Homo Sapiens.

## Objectives
- To identify homologous proteins using BLAST.
- To detect conserved domains using CDD/Pfam.
- To predict subcellular localization and function using GO annotation.
- To integrate all results to predict the possible function of the protein.

## Tools and Databases Used
- Python (Biopython)
- NCBI BLAST (blastp)
- NCBI Conserved Domain Database (CDD)
- UniProt
- Pfam
- QuickGO

---

## Input File
- input_sequence.fasta : FASTA file containing the protein sequence.

---

## Output Files
- blast_result.txt : Contains BLAST homology search results.
- functional_annotation.txt : Contains predicted functional annotation of the protein.
- homology_analysis.py : Python script used to perform BLAST.
- blast_result.xml : Contains raw BLAST outputin XML format.
- README.md : Project documentation.

---

## How to Run the Project
1. Install Biopython.
2. Save the protein sequence in FASTA format as input_sequence.fasta.
3. Run the Python script using:
   python homology_analysis.py
4. The BLAST result will be saved as blast_result.txt.
5. Perform domain analysis using NCBI CDD.
6. Write functional_annotation.txt based on BLAST, domain, and GO results.

---

##  Results Summary
- BLAST analysis showed strong similarity to uncharacterized proteins such as LOC728138 protein which is partial [synthetic construct ] from Homo sapiens and KIAA2013-like proteins with E-value = 0.0.
- Conserved domain analysis identified the DUF2152 domain (Pfam: pfam10222).
- GO annotation predicted membrane association with a transmembrane helix between residues 591–613.

## Conclusion
The selected protein (LOC728138) is a conserved, membrane-associated protein containing the DUF2152 domain. However, its precise biological function remains unknown. Further experimental validation is required to determine the precise biological function of this protein.

