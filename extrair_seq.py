IDPro = open('aaaaa.txt','r')
SeqPro = open('aspnid_pf00083_minuspenchr.fasta','r')
string_output = 'saida.fasta'

ID = IDPro.readlines()
Seq = SeqPro.readlines()
IDPro.close()
SeqPro.close()

i = 0
j = 0

#print(len(ID))
#print(len(Seq))

for i in range(len(ID)):
    #print(str(i)+' = '+ID[i])
    for j in range(len(Seq)):
        aux = j
        for char in ' \n':  
            line = ID[i].replace(char,'')
            if '>'+line+'\n' in Seq[aux]:
                output = open(string_output,'a')
                output.write(Seq[aux])
                output.close()
                aux = aux+1
                while not '>' in Seq[aux]:
                    output = open(string_output,'a')
                    output.write(Seq[aux])
                    output.close()
                    aux = aux+1
                    if aux == len(Seq):
                        output = open(string_output,'a')
                        output.write('\n')
                        output.close()
                        break
                break
            aux = j
