class Card:
    def __init__(self, name, surname, work, position, email):
        self.name = name
        self.surname = surname
        self.work = work
        self.position = position
        self.email = email

        # self._label_lenght  = 0
    
    # def label_lenght(self):
     #   return self._label_lenght
    
    # a = len(self.name)
    # def label_lenght_add(self, value=a):
    #     self._label_lenght += value

    def __str__(self):
        return f'{self.name} {self.surname} {self.work} {self.position} {self.email}'

# rozumiem, że to nie jest zmienna dynamiczna, ale nie byłem w stanie przypisać wszystkich potrzebnych danych powyżej
def lenght_of_name_and_surname(self):
    return (len(str(self.name)) + len(str(self.surname)) + 1)


def contact(self):
    return f" Kontaktuję się z {self.name} {self.surname} {self.position} {self.email}"

# card_list = [("Jan", "Kowalski", "Budowa", "Inżynier", "kowal@gmail.com"), ("Carmen", "Adams", "Oranges Records & Tapes", "Purchasing director", "CarmenTAdams@jourrapide.com"), ("Patricia", "Hazzard", "Dream Home", "Engineering", "PatriciaRHazzard@armyspy.com"), ("Michael", "Roussel", "Helios Air", "Pathologist", "MichaelCRoussel@dayrep.com"), ("Steven", "Kite", "Wag's", "Log debarker", "StevenKKite@armyspy.com")]

# for surname in card_list:
#    print(surname)

Kowalski = Card("Jan", "Kowalski", "Budowa", "Inżynier", "kowal@gmail.com")
Adams = Card("Carmen", "Adams", "Oranges Records & Tapes", "Purchasing director", "CarmenTAdams@jourrapide.com")
Hazzard = Card("Patricia", "Hazzard", "Dream Home", "Engineering", "PatriciaRHazzard@armyspy.com")
Roussel = Card("Michael", "Roussel", "Helios Air", "Pathologist", "MichaelCRoussel@dayrep.com")
Kite = Card("Steven", "Kite", "Wag's", "Log debarker", "StevenKKite@armyspy.com")

letters_count = lenght_of_name_and_surname(Kowalski)
print(letters_count)

contacts = contact(Kowalski)
print(contacts)


print()
cards = [Kowalski, Adams, Hazzard, Roussel, Kite]
for i in cards:
    print(i)
print()
by_name = sorted(cards, key=lambda person: person.name)
for a in by_name:
    print(a)
print()
by_surname = sorted(cards, key=lambda person: person.surname)
for b in by_surname:
    print(b)
print()
by_email = sorted(cards, key=lambda person: person.email)
for c in by_email:
    print(c)
print()