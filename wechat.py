#!/usr/bin/python
#_*_coding:utf-8 _*_
import requests,sys,json
import urllib3
urllib3.disable_warnings()

reload(sys)
sys.setdefaultencoding('utf-8')

def GetToken(Corpid,Secret):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Data = {
        "corpid":Corpid,
        "corpsecret":Secret
    }
    r = requests.get(url=Url,params=Data,verify=False)
    Token = r.json()['access_token']
    return Token

def SendMessage(Token,User,Agentid,Subject,Content):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
        "touser": User,                                 # 企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
        #"totag": Tagid,                                # 企业号中的部门id，群发时使用。
        "msgtype": "text",                              # 消息类型。
        "agentid": Agentid,                             # 企业号中的应用id。
        "text": {
            "content": Subject + '\n' + Content
        },
        "safe": "0"
    }
    r = requests.post(url=Url,data=json.dumps(Data),verify=False)
    return r.text


if __name__ == '__main__':
    User = sys.argv[1]                                                              # zabbix传过来的第一个参数
    Subject = sys.argv[2]                                                           # zabbix传过来的第二个参数
    Content = sys.argv[3]                                                           # zabbix传过来的第三个参数

    Corpid = "wx0f0c"                                                   # CorpID是企业号的标识
    Secret = "cecnGXBY"     # Secret是管理组凭证密钥
    #Tagid = "1"                                                                     # 通讯录标签ID
    Agentid = "1"                                                                   # 应用ID

    Token = GetToken(Corpid, Secret)
    Status = SendMessage(Token,User,Agentid,Subject,Content)
    print Status
