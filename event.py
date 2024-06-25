class Event:
    def __init__(self, name, date, counter):
        self.name = name
        self.date = date
        self.counter = counter

    def add_participant(self, new_participant):
        self.counter += new_participant

    def get_participant_count(self):
        print(f"There are currently {self.counter} participants at the event")