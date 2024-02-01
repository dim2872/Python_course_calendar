"""
Сущность, отвечающая за храние и предоставление данных
Оно хранит пользователей, календари и события.
Хранение в том числе означает сохранение между сессиями в csv файлах
(пароли пользователей хранятся как hash)

Должен быть статическим или Синглтоном

*) Нужно хранить для каждого пользователя все события которые с нима произошли но ещё не были обработаны.
"""
import csv
import hashlib

from Calendar import Calendar
from User import User


class Backend:
    _instance = None

    @staticmethod
    def get_instance():
        if not Backend._instance:
            Backend._instance = Backend()
        return Backend._instance

    def init(self):
        self.users = {}

    def load_data(self):
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                username, password = row
                self.users[username] = User(username, password)

    def save_data(self):
        with open('users.csv', 'w') as file:
            writer = csv.writer(file)
            for username, user in self.users.items():
                writer.writerow([username, user.password])

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if not user or not user.verify_password(password):
            return False
        return user
