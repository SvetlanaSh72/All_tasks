class Clients:
    def __init__(self, name, city, status, balance):
        self.name = name
        self.city = city
        self.status = status
        self.balance = balance


 #еще один пример вывода в строку
 #   def __str__(self):
 #       return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''

    def get_str_client(self):
        return f'имя: {self.name}, г.{self.city}, статус: {self.status}, баланс: {self.balance}'