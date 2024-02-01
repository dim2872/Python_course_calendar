from datetime import datetime

from Backend import Backend
from Interface import Interface

backend = Backend()
interface = Interface(backend)
interface.register("user1", "password1")
interface.create_event("Meeting", "Discuss upcoming project", {"user2", "user3"},
                       datetime.datetime(2021, 10, 1, 10), datetime.datetime(2021, 10, 1, 12))
interface.login("user1", "password1")
upcoming_events = interface.get_upcoming_events()
for event in upcoming_events:
    print(event.name, event.start, event.end)

interface.logout()