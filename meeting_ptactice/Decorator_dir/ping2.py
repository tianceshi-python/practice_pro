# encoding:utf-8
import paramiko
#import ssh

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect("192.186.0.2", username="root", password="123456")
    stdin, stdout, stderr = ssh.exec_command('ping www.baidu.com')
    res = stdout.read()
    print(res)
    if 'Received = 4' in res:
        print('ping 通')
    else:
        print('ping 不通')

except TimeoutError:
    print('由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。')
