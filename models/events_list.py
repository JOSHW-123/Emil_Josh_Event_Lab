from models.event import *

event1 = Event("01.07.2021", "Eminem", 1000, "SSE Hydro", "Concert")
event2 = Event("10.07.2021", "James Bond",20, "Cineworld", "Movie")
events = [event1, event2]

def add_new_event(event):
    events.append(event)