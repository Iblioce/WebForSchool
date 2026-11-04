import sys

user = input()

liste_mot = user.split()

nb_mot = len(liste_mot)


nb_lettre = 0
motMax = liste_mot[0]
max = liste_mot.count(motMax)
for mot in liste_mot:
    if liste_mot.count(mot)>max:
        max = liste_mot.count(mot)
        motMax = mot
    nb_lettre+=len(mot)

print("Nombre de mot : "+str(nb_mot)+" ;Nombre de lettre : "+str(nb_lettre)+"; le mot le plus présent est "+str(motMax))