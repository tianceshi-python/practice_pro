# encoding:utf-8

import subprocess

def ping(ip_dns):
    # coding:utf-8
    p = subprocess.Popen(["ping.exe",ip_dns],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    res = p.stdout.read().decode('gbk')
    print(res)

    if '已接受 = 4' in res:
        return ('ping 通')
    else:
        return ('ping 不通')

print(ping('www.baidu.com'))