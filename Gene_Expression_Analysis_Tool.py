from Bio import Entrez, SeqIO

Entrez.email = 'erfanzohrabi.ezm@gmail.com'  # provide your email for NCBI server
handle = Entrez.efetch(db='nucleotide', id='NM_000546', rettype='fasta', retmode='text')
seq_record = SeqIO.read(handle, 'fasta')
handle.close()

p53_seq = seq_record.seq


from Bio.Seq import Seq

p53_protein_seq = Seq(str(p53_seq)).translate()



from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW
from Bio import SearchIO
import os

# save p53 protein sequence to a fasta file
output_file = "p53_protein.fasta"
SeqIO.write(SeqRecord(p53_protein_seq, id="p53_protein"), output_file, "fasta")

# run InterProScan on the protein sequence
os.system("interproscan.sh -i " + output_file + " -f tsv")

# parse the InterProScan results
results_file = "p53_protein.tsv"
results = SearchIO.read(results_file, 'interproscan-tsv')
for hit in results:
    print(hit.id, hit.description, hit.evalue)
