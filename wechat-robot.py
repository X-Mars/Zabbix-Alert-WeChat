#!/usr/bin/python
# _*_coding:utf-8 _*_
# auther: X-Mars
# auther: 火星小刘

import sys, requests

subject = str(sys.argv[1])
message = str(sys.argv[2])
robot = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + sys.argv[3]

data = {
    'msgtype': 'markdown',
    'markdown': {
        'content': subject + '\n' + message
    }
}

response = requests.post(url=robot, json=data)

print(response.json())
