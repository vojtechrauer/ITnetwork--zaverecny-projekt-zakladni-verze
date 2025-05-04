from person import Person

class PersonManager:
    """A class to manage a list of Person objects.
    It allows adding, searching, and listing all persons.
    """
    def __init__(self):
        """Initialize the PersonManager with an empty list of persons."""
        self._person_list = []

    def list_all(self):
        """Return a list of all persons in the manager."""
        return self._person_list

    def add(self, person):
        """Add a Person object to the manager.
        The person must be an instance of the Person class.

        Args:
            person (Person): The Person object to add.

        Raises:
            ValueError: If the person is not an instance of the Person class.
        """
        if isinstance(person, Person):
            self._person_list.append(person)
        else:
            raise ValueError("Entered value must be of Person class")

    def search(self, first_name, last_name):
        """Search for a person by first name and last name.

        Args:
            first_name (str): The first name of the person to search for.
            last_name (str): The last name of the person to search for.

        Returns:
            list: A list of Person objects that match the search criteria.
        """
        search_list = [
            person
            for person in self._person_list
            if person.first_name.lower() == first_name.strip().lower()
            and person.last_name.lower() == last_name.strip().lower()
        ]
        return search_list