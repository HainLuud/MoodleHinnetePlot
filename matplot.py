import matplotlib.pyplot as plt
import numpy as np





#vastavalt            x             y                z
def tulpdiagram(sinu_koondhinne, kursuse_keskmine,  kursuse_nimed ):

    # Valikulised võib ära kustutada, ei mõjuta koodi tööd
    plt.xlabel('Kursused', fontsize=12) # x telje nimetus
    plt.ylabel('Protsent', fontsize=12) # y telje nimetus
    plt.title('Hinded') # Diagrammi pealkiri


    # Oluline, enne kustutamist konsulteerida Konstantinniga
    index = np.arange(len(kursuse_nimed)) # indeks ehk järjendi_suurus --> [0,1]
    plt.bar(index - 0.05, sinu_koondhinne,0.10, label='Sinu koondhinne') # SINU keskmise väärtus vastvalt indeksile
    plt.bar(index + 0.05, kursuse_keskmine,0.10, label="Kursuse keskmine") # KURSUSE keskmise väärtus vastvalt indeksile
    plt.xticks(index, kursuse_nimed, fontsize=12) # nimi vastvalt indeksile
    #plt.ylim([0,100]) # protsendi skaala, self explanatory
    plt.legend(loc='best') # Näitab legendi
    plt.gca().yaxis.grid(linestyle='dotted') # Näitab Y axis abistavaid jooni statistika jälgimiseks
    plt.show()



#näidis väärtused
#tulpdiagram([30,40,50,80],[50,60,50,70],["prog","arhit","sisse","mate pilt"])

# x = kursuse nimed 
# y väärtused


 