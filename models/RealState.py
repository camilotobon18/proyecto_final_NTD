class RealState:
    def __init__(self, title="", type_real_state="", address="", rooms=0, price=0.00, area=0, id_user=""):
        self.title = title
        self.type_real_state = type_real_state
        self.address = address
        self.rooms = rooms
        self.price = price
        self.area = area
        self.id_user = id_user

    def get_title(self):
        return self.title

    def get_type_real_state(self):
        return self.type_real_state
    
    def get_address(self):
        return self.address
    
    def get_rooms(self):
        return self.rooms

    def get_price(self):
        return self.price

    def get_id_user(self):
        return self.id_user

    
    def set_title(self, title):
        self.title = title
    
    def set_type_real_state(self, type_real_state):
        self.type_real_state = type_real_state

    def set_address(self, address):
        self.address = address
    
    def set_rooms(self, rooms):
        self.rooms = rooms

    def set_price(self, price):
        self.price = price
    
    def set_id_user(self, id_user):
        self.id_user = id_user