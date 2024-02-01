"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""
import hashlib


class User:
    def __init__init(self, login, username, password):
        self.login = login
        self.username = username
        self.password = self._hash_password(password)
        self.id = "@" + login
        self.calendar = None

    @staticmethod
    def _hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password == self._hash_password(password)