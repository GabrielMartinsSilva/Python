from Bio import SeqIO

for fasta in SeqIO.parse("my_seq.fasta.py","fasta"):
    print(fasta.id)#titulo da sequencia

    print (fasta.seq)#sequencia



