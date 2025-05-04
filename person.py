class Person:
    """
    Class representing a person with first name, last name, age, and phone number.
    """
    def __init__(self, first_name, last_name, age, phone_number):
        """Initialize a Person object with first name, last name, age, and phone number.
        The first name and last name are converted to title case.

        Args:
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.
            age (str): The age of the person as a string.
                It will be converted to an integer.
            phone_number (str): The phone number of the person.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.first_name.ljust(15)} {self.last_name.ljust(15)} {str(self.age).ljust(6)} {str(self.phone_number).ljust(12)}"

    def _validate_name(self, name, field_name):
        """Helper method to validate a name field.

        Args:
            name (str): The name to validate
            field_name (str): Name of the field for error message

        Returns:
            str: Validated and formatted name

        Raises:
            ValueError: If the name is invalid
        """
        name = name.strip()
        if name:
            return name.title()
        else:
            raise ValueError(f"Neplatna hodnota pro {field_name}")

    #first name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = self._validate_name(first_name, "krestni jmeno")

    #last name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = self._validate_name(last_name, "prijmeni")

    #age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        """Set the age of the person.

        Args:
            age (str): The age of the person as a string.
            It will be converted to an integer.

        Raises:
            ValueError: If the age is not a valid integer or is less than or equal to zero.
        """
        try:
            age = int(age)
        except:
            raise ValueError("Neplatna hodnota pro vek")

        if age > 0:
            self._age = age
        else:
            raise ValueError("Vek musi byt kladne cislo")

    #phone number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Set the phone number of the person.

        Args:
            phone_number (str): The phone number of the person.
            It will be stripped of leading and trailing whitespace.

        Raises:
            ValueError: If the phone number is empty or invalid.
        """

        phone_number = phone_number.strip()

        if phone_number:
            self._phone_number = phone_number
        else:
            raise ValueError("Neplatna hodnota pro telefonni cislo")


