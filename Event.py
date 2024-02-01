"""
Описывает некоторе "событие" - промежуток времени с присвоенными характеристиками
У события должно быть описание, название и список участников
Событие может быть единожды созданым
Или периодическим (каждый день/месяц/год/неделю)

Каждый пользователь ивента имеет свою "роль"
организатор умеет изменять названия, список участников, описание, а так же может удалить событие
участник может покинуть событие

запрос на хранение в json
Уметь создавать из json и записывать в него

Иметь покрытие тестами
Комментарии на нетривиальных методах и в целом документация
"""
import datetime
import json


class Event:
    def __init__(self, name, description, start_date, end_date, organizer):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.organizer = organizer
        self.participants = []

    def add_participant(self, user):
        self.participants.append(user)

    def remove_participant(self, user):
        self.participants.remove(user)

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.strftime('%Y-%m-%d %H:%M'),
            'end_date': self.end_date.strftime('%Y-%m-%d %H:%M'),
            'organizer': self.organizer,
            'participants': [participant.username for participant in self.participants]
        }

    @staticmethod
    def from_json(json_data):
        name = json_data['name']
        description = json_data['description']
        start_date = datetime.datetime.strptime(json_data['start_date'], '%Y-%m-%d %H:%M')
        end_date = datetime.datetime.strptime(json_data['end_date'], '%Y-%m-%d %H:%M')
        organizer = json_data['organizer']
        participants = json_data['participants']

        event = Event(name, description, start_date, end_date, organizer)
        for participant in participants:
            event.add_participant(participant)
        return event
