import requests
from models.User import User
class RequestsApi:

    url = "http://localhost:3000/"
    url_users = url+"user"

    @staticmethod
    def save_api(property):
        try:
            
            data = "{\"name\":\""+user.get_name()+" \",\"last_name\":\""+user.get_last_name()+" \",\"email\":\" "
            +user.get_email()+ " \",\"password\":\" "+user.get_password() +"}"
            #headers = {
            #    'content-type': "application/json",
            #    'x-api-key': "37172f24-8ea2-4faa-8306-4b6a364480c0"
            #}
            response = requests.request("POST", RequestsApi.url_users, data=data)
            if response.status_code != 200:
                return False
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