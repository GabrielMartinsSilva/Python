from Bio.Seq import Seq

my_seq = Seq('ATG')

#sequencia complementar
seq_complementar = my_seq.complement()
print("Sequencia complementar", seq_complementar)

# sequencia reversa complementar

seq_complementar_reversa = my_seq.reverse_complement()

print("Sequencia complementar reversa", seq_complementar_reversa)

#transcrição/sequencia de RNA

seq_rna = my_seq.transcribe()
print ("Fita de RNA", seq_rna)

#transformar RNA para DNA

seq_dna = seq_rna.back_transcribe()
print("Fita de RNA transforma em DNA", seq_dna)

#tradução/traduz uma sequencia de RNA mensageiro em uma sequencia de proteinas

seq_proteinaRNA = seq_rna.translate()
print("Aminoacido RNA", seq_proteinaRNA)

seq_proteinaDNA = seq_dna.translate()
print("Aminoacido DNA", seq_proteinaDNA)

#aplicando tradução a sequencia de DNA










