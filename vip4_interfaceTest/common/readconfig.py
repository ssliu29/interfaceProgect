#coding:utf-8

import  os
import configparser
import codecs

#获取文件的真实路径，然后分割路径和文件名存入一个元组
proDir = os.path.split(os.path.realpath(__file__))[0]
#获取上传目录
parDir = os.path.dirname(proDir)
configPath = os.path.join(parDir,"config.ini")
print(configPath)


class ReadConfig(object):
    def __init__(self, configPath=None):
        #1.实例化configparser对象
        self.cf = configparser.ConfigParser()
        #2.调用read方法读取该文件(传参：文件路径和编码格式)
        self.cf.read(configPath,encoding="utf-8-sig")

      #获取配置文件中的分组(eg:EMAIL)中的对应选项(eg:name)的值
    def get_email(self,name):
        #获取某某section下的value
        value = self.cf.get("EMAIL",name)
        return value

    def get_http(self,name):
        value = self.cf.get("HTTP",name)
        return value

    def get_db(self,name):
        value = self.cf.get("DATABASE",name)
        return value

