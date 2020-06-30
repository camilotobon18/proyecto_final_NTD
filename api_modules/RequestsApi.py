import requests
from models.Property import Property
class RequestsApi:

    url = "http://localhost:3000/"
    url_properties = url+"properties"

    @staticmethod
    def save_api(property):
        try:
            data = "{\"title\":\""+property.get_title_property()+" \",\"property_type\":\""+property.get_type_property()+" \",\"payment_type\":\""+property.get_payment_type()+" \",\"address\":\" "
            +property.get_address()+ " \",\"rooms\":\" "+property.get_rooms()+" \",\"price\":\""+property.get_type_price()+" \",\"area\":\""+property.get_area() +"}"
            
            response = requests.request("POST", RequestsApi.url_properties, data=data) #, headers=headers)
            if response.status_code != 200:
                return False
            else:
                return response.json()
        except:
            return False

    @staticmethod
    def get_all_api():
        try:
            response = requests.request("GET", RequestsApi.url_properties)#, headers=RequestsApi.headers)
            if response.status_code != 200:
                return True
            else:
                return response.json()
        except:
            return False
        
    @staticmethod
    def get_one_api(id):
        try:
            response = requests.request("GET", RequestsApi.url_properties + "/" + str(id))#, headers=RequestsApi.headers)
            if response.status_code != 200:
                return True
            else: 
                return response.json()
        except:
            return False
    
    @staticmethod
    def delete_api(id):
        try:
            response = requests.request("DELETE", RequestsApi.url_properties + "/" + str(id), headers=RequestsApi.headers)
            if response.status_code != 200:
                return True
            else:
                return response.json()
        except:
            return False
