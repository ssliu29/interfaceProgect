#coding:utf-8
import smtplib,time,os
from  email.mime.text import MIMEText
from  email.header import  Header

def send_mail_html(file):
    #发送HTML内容邮件
    #第一步：配置邮箱属性

    #发送邮箱
    sender = '15001012952@163.com'
    #接收邮箱
    receiver = '695846101@qq.com'
    #发送邮箱主题
    t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    subject = '接口自动化测试结果_' + t
    #发送邮箱服务器
    smtpserver = 'smtp.163.com'
    #发送邮箱用户/密码
    username = '15001012952@163.com'
    password = 'liusha29.'

    #读取html文件内容
    f =open(file,'rb')
    mail_body = f.read()
    f.close()

    #组装邮件内容和标题，中文需参数'utf-8',单字节字符不需要
    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    #第三步，登录并发送邮件
    try:
        #1.实例化stem类
        smtp = smtplib.SMTP()
        #2.连接stmp服务器
        smtp.connect(smtpserver)
        #3.登录邮箱
        smtp.login(username,password)
        #4.设置发件人，收件人，邮箱内容
        smtp.sendmail(sender,receiver,msg.as_string())
    except:
        print('邮箱发送失败')
    else:
        print('邮箱发送成功')
    finally:
        smtp.quit()

    def find_new_file(dir):
        #查找目录下最新的文件
        file_lists = os.listdir(dir)
        file_lists.sort(key=lambda fn:os.path.getmtime(dir + "\\" + fn)
                        if not os.path.isdir(dir + "\\" + fn)
                        else 0)
        print('最新的文件为：' + file_lists[-1])
        file = os.path.join(dir,file_lists[-1])
        print('完整文件路径:',file)
        return file

    dir = 'D:\\python_project\\vip4_interfaceTest\\testData'  #指定文件目录
    file = find_new_file(dir)  #查看最新的html文件
    file = "D:\\python_project\\vip4_interfaceTest\\testReport\\test.html"
    send_mail_html(file)  #发送html内容邮件