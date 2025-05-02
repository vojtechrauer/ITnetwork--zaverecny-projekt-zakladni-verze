from person import Person

class PersonManager:
    def __init__(self):
        self._person_list = []

    def list(self):
        return self._person_list

    def add(self, person):
        if isinstance(person, Person):
            self._person_list.append(person)
        else:
            print("Entered value must be of Person class")

    def search(self, first_name, last_name):
        search_list = [person for person in self._person_list if person.first_name == first_name and person.last_name == last_name]
        return search_list