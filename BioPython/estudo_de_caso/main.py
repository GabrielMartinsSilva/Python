entrada = open("16s_bacteria.fasta").read()
saida = open("bacteria.html","w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace("\n", "")

for k in range(len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1


#html

i=1
for k in cont:
    transparencia = cont[k]/max(cont.values())
    saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left;background-color:rgba(0,0,255, "+str(transparencia)+"')></div>")

    if i%4:
        saida.write("<div style='clear:both'></div>")
saida.close()
