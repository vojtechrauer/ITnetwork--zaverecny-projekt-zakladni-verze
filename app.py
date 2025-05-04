from person_manager import PersonManager
from console_ui import ConsoleUI

class App:
    """Main application class to run the insurance application.
    """
    def __init__(self):
        """Initialize the application with a PersonManager and ConsoleUI."""
        self._person_manager = PersonManager()
        self._console_ui = ConsoleUI(self._person_manager)

    def run(self):
        """Run the main application loop."""
        self._console_ui.main_menu()