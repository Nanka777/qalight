import json

import requests

class PageBookUsers:
    URL = 'http://demoqa.com'
    END_POINT = '/Account/v1/User'
    CUSTOM_USER_ENDPOINT = f'{END_POINT}/' + '{user_id}'

    def create_user(self, user_name, password):
        model = {
            "userName": user_name,
            "password": password
        }
        response = requests.post(url=self.URL + self.END_POINT, data=model)
        status = response.status_code
        assert status == 201
        new_user = json.loads(response.content)
        return {'name': new_user.get('username'), 'id': new_user.get('UserID')}

    def deleter_user(self, user_id):
        response = requests.delete(url=self.user + self.CUSTOM_USER_ENDPOINT)
        print(response.content)
