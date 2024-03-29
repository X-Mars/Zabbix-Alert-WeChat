#!/usr/bin/env python
# _*_coding:utf-8 _*_
# auther: X-Mars
# auther: 火星小刘

import sys, requests, json, time, hmac, hashlib, base64, urllib.parse

subject = str(sys.argv[1])
message = str(sys.argv[2])
robot_token = str(sys.argv[3])
secret = str(sys.argv[4])

timestamp = str(round(time.time() * 1000))
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

robot = 'https://oapi.dingtalk.com/robot/send?access_token=' + robot_token + '&timestamp=' + timestamp + '&sign=' + sign

data = {
    'msgtype': 'text',
    'text': {
        'content': subject + '\n' + message
    }
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url=robot, data=json.dumps(data), headers=headers)

print(response.json())
