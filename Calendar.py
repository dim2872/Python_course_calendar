"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""
import datetime


class Calendar:
    def __init__(self, user):
        self.user = user
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        self.events.remove(event)

    def get_events_in_range(self, start_date, end_date):
        events_in_range = []
        for event in self.events:
            if event.start_date <= end_date and event.end_date >= start_date:
                events_in_range.append(event)
        return events_in_range
