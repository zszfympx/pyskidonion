import requests
from datetime import datetime

class Skidonion:
    def __init__(self, uid: int, apitoken: str) -> None:
        self.uid = uid
        self.apitoken = apitoken
        self.URL = 'https://skidonion.tech/api/admin/'

    def getHeader(self) -> dict:
        """获取Header"""
        return {'phantom-shield-x-uid': self.uid, 'phantom-shield-x-api-token': self.apitoken}
    
    def userOnline(self, token: str) -> dict:
        """验证TOKEN是否在线"""
        params = dict()
        params['software_id'] = 96
        params['token'] = token
        response = requests.post(self.URL+'user-online', params=params, headers=self.getHeader())
        if(response.status_code!=200):
            return None
        else:
            if response.json()['message']=='无效的Token':
                return None
            else:
                return response.json()
            
    def userInfomation(self, username: str, softwareid: int) -> dict:
        """获取用户基本信息"""
        params = dict()
        params['software_id'] = softwareid
        params['username'] = username
        response = requests.post(self.URL+'user-information', params=params, headers=self.getHeader())
        if response.status_code!=200:
            return None
        else:
            return response.json()
