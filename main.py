from vehicle import Vehicle
from event import Event
vehicle = Vehicle("7AKN145", "Toyota", "Nicolas")
vehicle.display_info()
vehicle.update_owner("Andres")
vehicle.display_info()

event = Event("Nicolas", "6/25/2024", 1)
event.add_participant(5)
event.get_participant_count()






