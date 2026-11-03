import sys

list_course = list()

user = 9999
while(int(user)!=4):
    print("1-ajouter un element\n2-supprimer un element\n3-afficher la liste\n4-Sortir")
    user = input()
    try:
        match int(user):
            case 1:
                print("Entrez un element !")
                ele = input()
                list_course.append(ele)
            case 2:
                index = int(input())
                list_course.pop(index)
            case 3:
                print(list_course)
    except ValueError:
        print("Erreur : Entrée invalide")
        sys.exit(1)
