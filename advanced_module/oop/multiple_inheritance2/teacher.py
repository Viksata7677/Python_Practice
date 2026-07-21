from multiple_inheritance2.employee import Employee
from multiple_inheritance2.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'