class Property:
    def __init__(self, title_property="", type_property="", payment_type="", address="", rooms=0, price=0.00, area=0, property_image="", id_user=""):
        self.title_property = title_property
        self.type_property = type_property
        self.payment_type = payment_type
        self.address = address
        self.rooms = rooms
        self.price = price
        self.area = area
        self.property_image = property_image
        self.id_user = id_user

    def get_title_property(self):
        return self.title_property

    def get_type_property(self):
        return self.type_property

    def get_payment_type(self):
        return self.payment_type
    
    def get_address(self):
        return self.address
    
    def get_rooms(self):
        return self.rooms

    def get_price(self):
        return self.price
    
    def get_property_image(self):
        return self.property_image

    def get_id_user(self):
        return self.id_user


    
    def set_title_property(self, title_property):
        self.title_property = title_property
    
    def set_type_property(self, type_property):
        self.type_property = type_property
    
    def set_payment_type(self, payment_type):
        self.payment_type = payment_type

    def set_address(self, address):
        self.address = address
    
    def set_rooms(self, rooms):
        self.rooms = rooms

    def set_price(self, price):
        self.price = price
    
    def set_property_image(self, property_image):
        self.property_image = property_image
    
    def set_id_user(self, id_user):
        self.id_user = id_user