from person import Person
from person_manager import PersonManager
from console_ui import ConsoleUI

class App:
    def __init__(self):
        self._person_manager = PersonManager()
        self._console_ui = ConsoleUI(self._person_manager)

    def run(self):
        self._console_ui.main_menu()

        choice = input()

        match choice:
            case "1":
                self._console_ui.add_person_menu()
            case "2":
                self._console_ui.display_all_people()
            case "3":
                self._console_ui.get_search_values()
            case "4":
                pass