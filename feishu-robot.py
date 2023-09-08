#!/usr/bin/env python
# _*_coding:utf-8 _*_
# auther: X-Mars
# auther: 火星小刘

import sys, requests, json

subject = str(sys.argv[1])
message = str(sys.argv[2])
robot_token = str(sys.argv[3])

robot = 'https://open.feishu.cn/open-apis/bot/v2/hook/' + robot_token

data = {
    'msg_type': 'text',
    'content': {
        'text': subject + '\n' + message
    }
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url=robot, data=json.dumps(data), headers=headers)

print(response.json())

