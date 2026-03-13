from src.models.exceptions import ValidationError

class User:
    def __init__(self, name, email):
        self.name = name
        self._email = ''
        self.set_email(email)



    def get_info(self):
        return f'Пользователь: {self.name}, Email: {self.email}'


    def set_email(self, email):
        if '@' not in email:
            raise ValidationError('Неверный формат email')
        self._email = email


    def __str__(self):
        return self.name