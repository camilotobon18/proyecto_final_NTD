import requests
from models.Vote import Vote
class RequestsApi:

    url = "http://api.thecatapi.com/v1/votes"
    headers = {'x-api-key': "37172f24-8ea2-4faa-8306-4b6a364480c0"}

    @staticmethod
    def save_api(vote):
        try:
            #data = "{\"name\":\""+user.get_name()+" \",\"last_name\":\""+user.get_last_name()+" \",\"email\":\" "
            #+user.get_email()+ " \",\"password\":\" "+user.get_password() +"}"
            data = "{\"image_id\":\""+vote.get_image_id()+"\",\"sub_id\":\""+vote.get_sub_id()+"\",\"value\":\""+str(vote.get_value())+"\"}"
            headers = {
                'content-type': "application/json",
                'x-api-key': "37172f24-8ea2-4faa-8306-4b6a364480c0"
            }
            response = requests.request("POST", RequestsApi.url, data=data, headers=headers)
            if response.status_code != 200:
                return False
            else:
                return response.json()
        except:
            return False

    @staticmethod
    def get_all_api():
        try:
            response = requests.request("GET", RequestsApi.url, headers=RequestsApi.headers)
            if response.status_code != 200:
                return True
            else:
                return response.json()
        except:
            return False
        
    @staticmethod
    def get_one_api(id):
        try:
            response = requests.request("GET", RequestsApi.url + "/" + str(id), headers=RequestsApi.headers)
            if response.status_code != 200:
                return True
            else: 
                return response.json()
        except:
            return False
    
    @staticmethod
    def delete_api(id):
        try:
            response = requests.request("DELETE", RequestsApi.url + "/" + str(id), headers=RequestsApi.headers)
            if response.status_code != 200:
                return True
            else:
                return response.json()
        except:
            return False
