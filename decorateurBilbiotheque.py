import time

# calcule du temps
def perf(fonction):
    def wrapper(*args, **kwargs):
        debut = time.perf_counter()
        fonction(*args, **kwargs)
        fin = time.perf_counter()
        temps = fin-debut
        print(f"temps écoulé : {temps:.8f} s")
    return wrapper

class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Library():
    def __init__(self):
        self.listLivres = list()

    def add_book(self,b):
        self.listLivres.append(b)

    def remove_book(self,b):
        self.listLivres.pop(b)

    def print_books(self):
        for book in self.listLivres :
            print(book.title+" écrit par "+book.author)
    @perf
    def new_print_books(self):
        for book in self.listLivres :
                    print(book.title+" écrit par "+book.author)





#test
b1 = Book("Le petit prince","Antoine de saint-exupéry") # presque fini
b2 = Book("Tant que le café est encore chaud","川口 俊和") #je ne l'ai pas encore lu ...
lib = Library()

lib.add_book(b1)
lib.add_book(b2)
#lib.print_books()
lib.new_print_books()