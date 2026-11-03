import sys
print("Choissisez entre addition, soustraction, multiplication, division")

user = input()
print("Opération prise en compte.")
print("Entrez votre première puis votre deuxième valeur !")
try:
    user_1 = int(input())
    user_2 = int(input())
except ValueError:
    print("Erreur : Entrée invalide")
    sys.exit(1)

if(user == "x" or user=="multiplication"):
    print(user_1*user_2)
elif (user=="+" or user=="addition"):
    print(user_1+user_2)
elif (user=="-" or user=="soustraction"):
    print(user_1-user_2)
elif (user=="/" or user=="division"):
    try:
        print(user_1/user_2)
    except ZeroDivisionError:
        print("Erreur : Division par 0")
        sys.exit(1)