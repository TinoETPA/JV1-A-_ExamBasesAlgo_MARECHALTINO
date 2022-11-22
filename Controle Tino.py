#Partie 1 - Tri à bulles
#1 Programme permettant de permuter deux valeurs du tableau.

nombresmax = 89
nombresmin = 16
myTable=[89,35,56,42,16]
for i in range(len(myTable)):
    if(nombresmin < myTable[0]):
        myTable[0] = nombresmin
        myTable[4] = nombresmax
print(myTable)

#2 Programme permettant le parcours du tableau au cours d'une itération du tri à bulles.

nombresmax = 89
nombresmin = 16
myTable = [89,35,56,42,16]
for j in range(len(myTable)):
    if(nombresmax > myTable[j]):
        myTable[4] = nombresmax
for i in range(j,len(myTable)):
        if(nombresmin > myTable[i]):
             myTable[0] = nombresmin
print(myTable)

#3 Programme implémentant le tri à bulles complet.

#4 Le tri à bulles est considéré comme très lent car il vérifie nombre par nombre la totalité des valeurs présente dans le tableau.
#Le but est de remplacer les valeurs dans un orde croissant, cela prend donc beaucoup de temps car cela ne s'arrête pas tant que toutes les valeurs n'ont pas été correctement en orde croissant.
#On peux facilement estimer son ordre de grandeur on regardant le nombres de valeurs présente de le tableau.

#Partie 2 - Tic tac toe

