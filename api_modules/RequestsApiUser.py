import requests
from models.User import User
class RequestsApiUser:

    url = "http://localhost:3000/"
    url_users = url+"user"

    @staticmethod
    def save_api(user):
        try:
            
            data = "{\"email\":\" "+user.get_email()+ " \",\"password\":\" "+user.get_password() +"}"
            
            response = requests.post(RequestsApiUser.url_users+"/signup/", data=data)
            if response.status_code != 200:
                return response.text
            else:
                return response.json()
        except:
            return False

    @staticmethod
    def get_one_api(id):
        try:
            response = requests.request("GET", RequestsApiUser.url_properties + "/" + str(id))#, headers=RequestsApi.headers)
            if response.status_code != 200:
                return True
            else: 
                return response.json()
        except:
            return False
    
    @staticmethod
    def delete_api(id):
        try:
            response = requests.request("DELETE", RequestsApiUser.url_properties + "/" + str(id), headers=RequestsApi.headers)
            if response.status_code != 200:
                return True
            else:
                return response.json()
        except:
            return False