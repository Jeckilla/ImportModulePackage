from Application.db.db import peoples


class Employees():

    def __init__(self):
        print("Класс сотрудников")

    def get_employees(self):
        for people in peoples:
            for key, value in people.items():
                print(key, value)
