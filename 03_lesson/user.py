class User:
    """Класс пользователя.
    Аттрибуты:
    - first_name - Имя;
    - last_name - Фамилия
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        """Метод печати имени"""
        print(f"Имя: {self.first_name}")

    def print_last_name(self):
        """Метод печати фамилии"""
        print(f"Фамилия: {self.last_name}")

    def print_full_name(self):
        """Метод печати полного имени"""
        print(f"Полное имя: {self.first_name} {self.last_name}")
