import sys
print("entrez un nombre")
a = input()
try :
    if(int(a)%2):
        print("Impaire")
    else:
        print("paire")
except ValueError:
    print("Erreur : Entrée invalide")
    sys.exit(1)
    