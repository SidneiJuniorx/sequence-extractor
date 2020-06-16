IDPro = open('Aspnid_stids.txt','r')
SeqPro = open('Aspnid_proteins.fa','r')

ID = IDPro.readlines()
Seq = SeqPro.readlines()
IDPro.close()
SeqPro.close()

i = 0
j = 0

for i in range(len(ID)):
    #print(line)
    for j in range(len(Seq)):
        aux = j
        for char in ' \n':  
            line = ID[i].replace(char,'')
            if '>'+line+'\n' in Seq[aux]:
                output = open('aspnid_sugar_transporters.fasta','a')
                output.write(Seq[aux])
                output.close()
                aux = aux+1
                while not '>' in Seq[aux]:
                    output = open('aspnid_sugar_transporters.fasta','a')
                    output.write(Seq[aux])
                    output.close()
                    aux = aux+1
                break
        aux = j
