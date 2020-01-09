#coding:utf-8

import requests
import json

class ConfigHttp(object):

    def __init__(self):
        #print('开始请求接口')
        print('请求接口完成')


    def get(self,url,param):
        getresult = requests.get(url = url, params = param)
        dict = getresult.json()
        print('get接口返回的结果:',getresult.text)
        errorcode = dict['errorCode']
        print('get请求接口的errorcode码：',errorcode)
        return errorcode

    def post(self,url,data):
        postresult = requests.post(url = url, data = eval(data))
        print('post接口返回的结果：',postresult.text,type(postresult.text))
        dict1 = json.loads(postresult.text)
        errorcode = dict1['errorCode']
        print('errorcode状态码：',errorcode)
        return errorcode

    def put(self):
        print('put请求接口完成')
        pass

if __name__ == '__main__':
    con = ConfigHttp()
    #data={'username':'liangchao','password':'123456'}
    #con.post('https://www.wanandroid.com/user/login',data=data)
    # param = {'username':'liangchao'}
    # con.get('https://www.wanandroid.com/user/logout/json',param = param)