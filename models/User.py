class User():

    def __init__(self, name="", last_name="", email="", password=""):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password 
    
    def get_name(self):
        return self.name
    
    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password


    def set_name(self, name):
        self.name = name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def set_email(self, email):
        self.email = email
    
    def set_password(self, password):
        self.password = password


