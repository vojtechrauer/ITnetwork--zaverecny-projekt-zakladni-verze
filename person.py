class Person:
    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.first_name.ljust(15)} {self.last_name.ljust(15)} {str(self.age).ljust(6)} {str(self.phone_number).ljust(12)}"

    def __repr__(self):
        return f"{self.first_name.ljust(15)} {self.last_name.ljust(15)} {str(self.age).ljust(6)} {str(self.phone_number).ljust(12)}"

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def age(self):
        return self._age

    @property
    def phone_number(self):
        return self._phone_number

    @first_name.setter
    def first_name(self, first_name):
        if len(first_name) > 0 and first_name.isalpha():
            self._first_name = first_name.lower().capitalize()
        else:
            print("Invalid value for first name")

    @last_name.setter
    def last_name(self, last_name):
        if len(last_name) > 0 and last_name.isalpha():
            self._last_name = last_name.lower().capitalize()
        else:
            print("Invalid value for last name")

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            print("invalid value for age")

    @phone_number.setter
    def phone_number(self, phone_number):
        if isinstance(phone_number, int) and phone_number > 0:
            self._phone_number = phone_number
        else:
            print("invalid value for phone number")


