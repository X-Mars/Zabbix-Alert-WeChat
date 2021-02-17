#!/usr/bin/python3

import os,sys
import requests,json
import urllib3
urllib3.disable_warnings()
import importlib

importlib.reload(sys)
#Cache in Memory 
CacheFile = '/dev/shm/zabbix_wechat_config.json'


def GetToken(Corpid,Secret):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Payload = {
        "corpid":Corpid,
        "corpsecret":Secret
    }
    #Initial Cache
    if not os.path.exists(CacheFile):
        with open(CacheFile, 'w'): pass

    if not os.stat(CacheFile).st_size == 0:
        with open(CacheFile,'r') as file:
                Token = json.load(file)['access_token']
                return Token
    else:
        try:
            r = requests.get(url=Url,params=Payload,verify=False)
            if r.status_code == 200:
                if r.json()['errcode'] == 0:
                    Token = r.json()['access_token']
                    with open(CacheFile, 'w') as file:
                        file.write(r.text)
                    return Token
                else:
                    print(r.json()['errcode'])
            else:
                print(r.status_code)
        except Exception as err:
            print('Erorr Code:',str(err))

def SendMessage(Token,User,Agentid,Subject,Content):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Payload = {
        # 企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
        "touser": User,
        # 企业号中的标签id，群发使用（推荐）
        #"totag": Tagid,
        # 企业号中的部门id，群发时使用。
        "toparty": Partyid,
        # 消息类型。
        "msgtype": "text",
        # 企业号中的应用id。
        "agentid": Agentid,
        "text": {
            "content": Subject + '\n' + Content
        },
        "safe": "0"
    }
    try:
        r = requests.post(url=Url,data=json.dumps(Payload),verify=False)
        if r.status_code == 200:
            if r.json()['errcode'] == 0:
                return r.json()['errcode']
            #Access_token expired ,response error code 40014 and 42001,then refresh Cache.
            elif (r.json()['errcode'] == 40014) or (r.json()['errcode'] == 42001):
                with open(CacheFile, 'w'): pass
                return r.json()['errcode']
            else:
                return r.json()['errcode']
        else:
            print(r.status_code)
    except Exception as err:
        print('Erorr Code:',str(err))

if __name__ == '__main__':

    User = sys.argv[1]
    Subject = sys.argv[2]
    Content = sys.argv[3]

    # CorpID
    Corpid = "wxaf"
    # Secret
    Secret = "aKDdCRT76"
    # 通讯录标签ID
    #Tagid = "1"
    # 应用ID
    Agentid = "1000001"
    # 部门ID
    Partyid = "1"

    try:
        Token = GetToken(Corpid, Secret)
        Status = SendMessage(Token,User,Agentid,Subject,Content)
        #While access_token expired refresh Cache try again.
        if Status == 40014 or Status == 42001:
            Token = GetToken(Corpid, Secret)
            Status = SendMessage(Token,User,Agentid,Subject,Content)
        else:
            print(Status)
    except Exception as err:
        print('Erorr Code:',str(err))
