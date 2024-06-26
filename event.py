class Event:
    def __init__(self, name, date, attendance):
        self.name = name
        self.date = date
        self.attendance = attendance

    def add_participant(self, new_participant):
        self.attendance += new_participant

    def get_participant_count(self):
        print(f"There are currently {self.counter} participants at the event")