import sys,random

rng = random.randrange(100)
try:
    user = input()
    intUser = int(user)
    while(intUser!=rng):
        if(rng>intUser):
            print("plus haut")
        else:
            print("plus bas")
        user = input()
        intUser = int(user)
except ValueError:
        print("Erreur : Entrée invalide")
        sys.exit(1)
print("bonne réponse !")
