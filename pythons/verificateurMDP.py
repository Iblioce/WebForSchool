import sys
print("entrez un MDP")
mdp = input()
print("entrez a nouveau votre MDP")
user = input()
if(mdp==user):
    print("bon mot de passe")
else:
    print("mauvais mdp")