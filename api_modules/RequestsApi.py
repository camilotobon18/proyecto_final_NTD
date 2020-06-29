import requests
from models.Property import Property
class RequestsApi:

    #url = "http://api.thecatapi.com/v1/votes"
    url = "http://localhost:3000/"
    url_properties = url+"properties"
    url_users = url+"user"
    #headers = {'x-api-key': "37172f24-8ea2-4faa-8306-4b6a364480c0"}

    @staticmethod
    def save_api(property):
        try:
            data = "{\"title\":\""+property.get_title_property()+" \",\"property_type\":\""+property.get_type_property()+" \",\"payment_type\":\""+property.get_payment_type()+" \",\"address\":\" "
            +property.get_address()+ " \",\"rooms\":\" "+property.get_rooms()+" \",\"price\":\""+property.get_type_price()+" \",\"area\":\""+property.get_area() +"}"
            #data = "{\"name\":\""+user.get_name()+" \",\"last_name\":\""+user.get_last_name()+" \",\"email\":\" "
            #+user.get_email()+ " \",\"password\":\" "+user.get_password() +"}"
            #data = "{\"image_id\":\""+vote.get_image_id()+"\",\"sub_id\":\""+vote.get_sub_id()+"\",\"value\":\""+str(vote.get_value())+"\"}"
            #headers = {
            #    'content-type': "application/json",
            #    'x-api-key': "37172f24-8ea2-4faa-8306-4b6a364480c0"
            #}
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
