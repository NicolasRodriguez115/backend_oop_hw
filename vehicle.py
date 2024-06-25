class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.regisrtation_number = reg_num
        self.type = type
        self.owner = owner

    def display_info(self):
        print(f"Registration Number: {self.regisrtation_number}")
        print(f"Type: {self.type}")
        print(f"Owner: {self.owner}")

    def update_owner(self, new_owner):
        self.owner = new_owner
    

