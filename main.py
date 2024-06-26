from vehicle import Vehicle
from event import Event
veh_1 = Vehicle("7AKN145", "Toyota", "Nicolas")
veh_1.display_info()
veh_1.update_owner("Andres")
veh_1.display_info()

veh_2 = Vehicle("9GIO426", "Kia", "Dakota")
veh_2.display_info()
veh_2.update_owner("Deacon")
veh_2.display_info()


veh_3 = Vehicle("3TRP527", "BMW", "Jhon")
veh_3.display_info()
veh_3.update_owner("Paul")
veh_3.display_info()

event = Event("Nicolas", "6/25/2024", 1)
event.add_participant(5)
event.get_participant_count()






