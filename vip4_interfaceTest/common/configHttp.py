#coding:utf-8

import requests

class configHttp(object):

    def __init__(self):
        print('开始请求接口')
        print('请求接口完成')


    def get(self,url,param):
        getresult = requests.get(url = url, params = param)
        print('get请求接口完成')
        return getresult

    def post(self,url,data):
        postresult = requests.post(url = url, data = data)
        print('post请求接口完成')
        return postresult

    def put(self):
        print('put请求接口完成')
        pass

