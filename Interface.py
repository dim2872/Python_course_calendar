"""
Позволяет зайти по логину-паролю или создать нового пользователя (а так же выйти из аккаунта)
Позволяет выбрать календарь, узнать ближайшие события, события из промежутка времени а так же
Создать событие или удалить событие
После создания события можно добавить туда пользователей
Если нас добавили в событие или удалили мы получаем уведомление.

в main можно использовать ТОЛЬКО interface
"""
from datetime import datetime

from Backend import Backend
from Calendar import Calendar
from Event import Event
from User import User


class Interface:
    def init(self):
        self.backend = Backend.get_instance()
        self.current_user = None

    def login(self, username, password):
        user = self.backend.authenticate_user(username, password)
        if user:
            self.current_user = user
            print("Login successful!")
        else:
            print("Invalid username or password.")

    def create_user(self, username, password):
        if username in self.backend.users:
            print("Username already exists.")
        else:
            user = User(username, password)
            self.backend.users[username] = user
            self.backend.save_data()
            print("User created successfully.")

    def logout(self):
        self.current_user = None
        print("Logged out successfully.")

    def select_calendar(self):
        if self.current_user:
            return Calendar(self.current_user)
        else:
            print("You need to login first.")

    def get_upcoming_events(self, calendar):
        current_date = datetime.datetime.now()
        upcoming_events = []
        for event in calendar.events:
            if event.start_date >= current_date:
                upcoming_events.append(event)
        return upcoming_events

    def get_events_in_range(self, calendar, start_date, end_date):
        events_in_range = calendar.get_events_in_range(start_date, end_date)
        return events_in_range

    def create_event(self, calendar, name, description, start_date, end_date):
        if self.current_user != calendar.user:
            print("You can only create events in your own calendar.")
            return


