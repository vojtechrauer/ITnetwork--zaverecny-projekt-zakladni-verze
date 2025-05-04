from person import Person

class ConsoleUI:
    """A class to manage the console user interface for the insurance application.
    It provides methods to display menus, add persons, and search for persons.
    """
    def __init__(self, person_manager):
        """Initialize the ConsoleUI with a PersonManager instance."""
        self._person_manager = person_manager

    def main_menu(self):
        """Display the main menu and handle user input."""
        app_run = True
        while app_run:

            print("------------------------------------")
            print("Evidence pojistenych")
            print("------------------------------------")
            print("Vyberte si akci:")
            print("1 - Pridat noveho pojisteneho")
            print("2 - Vypsat vsechny pojistence")
            print("3 - Vyhledat pojisteneho")
            print("4 - Konec")

            choice = input()

            match choice:
                case "1":
                    self.add_person_menu()
                case "2":
                    self.display_all_people()
                case "3":
                    self.search_people_menu()
                case "4":
                    print("Dekuji za pouziti aplikace")
                    app_run = False
                case _:
                    print("Neplatna volba, zadejte prosím pouze cislice od 1 do 4")
    def add_person_menu(self):
        """Display the menu for adding a new person."""
        first_name = input("Zadejte krestni jmeno: ")
        last_name = input("Zadejte prijmeni: ")
        age = input("Zadejte vek: ")
        phone_number = input("Zadejte telefonni cislo: ")

        try:
            person = Person(first_name, last_name, age, phone_number)
            self._person_manager.add(person)

            print("Data byla ulozena, pokracujte stisknutim libovolne klavesy")
        except ValueError as e:
            print("Pri vkladani dat vznikla nasledujici chyba: ", e)

        input()


    def search_people_menu(self):
        """Display the menu for searching a person."""
        first_name = input("Zadejte krestni jmeno: ")
        last_name = input("Zadejte prijmeni: ")
        search_results = self._person_manager.search(first_name, last_name)

        self.display_people(
            search_results,
            "Seznam hledanych pojistencu",
            "Zadanym kriteriim neodpovida zadny pojistenec",
        )
        
    def display_all_people(self):
        """Display all persons in the manager."""
        person_list_all = self._person_manager.list_all()
        
        self.display_people(
            person_list_all,
            "Seznam vsech pojistencu",
            "Zadny pojistenec nebyl nalezen",
        )

    def display_people(self, person_list, heading, empty_message):
        """Display a list of persons with a heading and an empty message.

        Args:
            person_list (list): List of Person objects to display.
            heading (str): The heading for the display.
            empty_message (str): Message to display if the list is empty.
        """
        print(heading)
        print("-------------------------")

        if len(person_list) > 0:
            people_list_print = f""
            for person in person_list:
                people_list_print += f"{person}\n"
            print(people_list_print)
        else:
            print(empty_message)

        input()


