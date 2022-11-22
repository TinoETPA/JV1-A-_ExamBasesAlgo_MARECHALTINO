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
#Le but est de remplacer les valeurs dans un orde croissant, cela prend donc beaucoup de temps car cela ne s'arrête pas tant que toutes les valeurs n'ont pas été correctement mis en orde croissant.
#On peux facilement estimer son ordre de grandeur on regardant le nombres de valeurs présente de le tableau.

#Partie 2 - Tic tac toe

#1 Ecrire la fonctionnalité permettant d’afficher la grille de jeu.

print("__!__!__")
print("__!__!__")
print("__!__!__")

Joueur1 = ("O")
Joueur2 = ("X")

#2 Écrire la fonctionnalité permettant de jouer un O ou un X.


#3 Écrire la fonctionnalité vérifiant si oui ou non l’un des joueurs a réussi à aligner 3 symboles sur une ligne verticale, horizontale, diagonale.



#4. Écrire la fonctionnalité vérifiant si la grille est complète.



#5. Écrire un programme permettant de jouer à deux au Tic tac toe.



#6. Qu’aura-t-on besoin de faire, si on souhaite désormais programmer un jeu de Puissance 4 ? Répondez en commentaire.
#Si on souhaite désormais programmer un jeu de Puissance 4, il faudra faire un programme qui fait en sorte que lorsqu'on choisi où placer le pion sur la colonne, qu'il tombe dans la colonne et s'arrête au bon endroit (c'est à dire  soit au niveau du "sol" soit juste au dessus d'un autre pion).



#Je comprend rien à la programmation, même en essayant de rattraper les deux cours précédent je n'y arrive vraiment pas, même en suivant les cours j'ai déjà beaucoup de mal alors rattraper les cours c'est l'équivalent pour moi d'essayer de lire un livre en chinois...