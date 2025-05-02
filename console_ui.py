from person import Person
from person_manager import PersonManager
from app import App
class ConsoleUI:
    def __init__(self, person_manager):
        self._person_manager = person_manager

    def main_menu(self):
        print("""
------------------------------------
Evidence pojistenych
------------------------------------
Vyberte si akci:
    1 - Pridat noveho pojisteneho
    2 - Vypsat vsechny pojistence
    3 - Vyhledat pojisteneho
    4 - Konec
            """)

    def add_person_menu(self):
        first_name = input("Zadejte krestni jmeno")
        last_name = input("Zadejte prijmeni")
        age = input("Zadejte vek")
        phone_number = input("Zadejte telefonni cislo")

        person = Person(first_name, last_name, age, phone_number)
        self._person_manager.add(person)

        print("Data byla ulozena, pokracujte stisknutim libovolne klavesy")
        input()

        self.main_menu()

    def display_all_people(self):
        print("Seznam vsech pojistencu")
        print("-------------------------")
        people_list_print = f""
        for person in self._person_manager.list():
            people_list_print += f"{person}\n"
        print(people_list_print)


    def display_searched_people(self):
        print("Seznam hledanych pojistencu")
        print("----------------------")
        searched_people_list = f""
        for person in self._person_manager.search():
            searched_people_list += f"{person}\n"

    def search_people_menu(self):
        first_name = input("Zadejte krestni jmeno")
        last_name = input("Zadejte prijmeni")
        self._person_manager.search()


