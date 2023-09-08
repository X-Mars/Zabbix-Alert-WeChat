#!/usr/bin/env python
# _*_coding:utf-8 _*_
# auther: X-Mars
# auther: 火星小刘

import sys, requests, json, time, hmac, hashlib, base64, urllib.parse

# 钉钉接口加密鉴权
# secret 在机器人管理页面设置，勾选加签后，复制秘钥
timestamp = str(round(time.time() * 1000))
secret = '需要替换这里'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

subject = str(sys.argv[1])
message = str(sys.argv[2])
# robot_token 为机器人地址中的xxxxxxxxxxx   https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxxxxx

robot_token = str(sys.argv[3])
robot = "https://oapi.dingtalk.com/robot/send?access_token=" + robot_token + "&timestamp=" + timestamp + "&sign=" + sign

data = {
    "msgtype": "text",
    "text": {
        "content": subject + "\n" + message
    }
}
headers = {'Content-Type': 'application/json'}


response = requests.post(url=robot, data=json.dumps(data), headers=headers)

print(response.json())
