# dokumentariji je aplikacija za ispis i unos studenata
# na kolegiju razvoj poslovnih aplikacija
from DokumentarijiError import DokumentarijiError
class Dokumentariji: 
    def __init__(self):
        self.names = ''

    def display_title_bar(self):
        print("\t***************************************************")
        print("\t*** Dokumentariji - Razvoj poslovnih aplikacija ***")
        print("\t***************************************************")

    def get_user_choice(self):
        # ispisujemo korisniku meni što može raditi u aplikaciji
        # na kraju ga pitamo i uzimamo njegov odabir te taj odabir vraćamo 
        print("\n[1] Pogledaj listu studenata.")
        print("[2] Dodaj novog studenata.")
        print("[x] Izlaz.")
        
        return input("Što želite napraviti u dokumentariju?")
        

    def show_names(self):
        # prikazuje imena svih studenata dodanih u listu
        print("\n Ovo je popis studenata na koleiju Razvoj poslovnih aplikacija 2019/2020: \n")

        for name in self.names:
            print(name.title())

    def  get_new_name(self):
        # uzimamo kroz input od korisnika novo ime te ga dodajemo u listu ako to ime već nije u listi
        new_name = input("\nUnesite ime studenta: ")
        if new_name in self.names:
            print("\n{} je već upisan/a u dokumenatriju!".format(new_name.titiel()))
        elif new_name in self.names: 
            print("Unesi ime:")
        else:
            self.names.append(new_name)
            print("\nDobrodošao/la {}!\n".format(new_name.title()))
        
    def play(self):  # VJEŽBA staviti početnu inicijalizaciju varijable names u init metodu (konstruktor) klase Dikuentariji
        self.names = []
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
               self.show_names()
            elif choice == '2':
                self.get_new_name()
            elif choice == 'x':
                print("\n Hvala na pregledu/uređivanju dokumentarija. Pozdrav.")    
            else:
                self.get_user_choice = ''
                raise DokumentarijiError(101)
            

if __name__ == "__main__":
   game = Dokumentariji()
   game.play()
        


