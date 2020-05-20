# encoding:utf-8


'''
今天在用Streaming-Python处理一个MapReduce程序时，发现reducer失败，原因为耗费内存达到极限了！
仔细查看代码时，发现有一个集合里保存着URL，而URL长度是比较长的，直接保存确实是耗费内存，
于是想到用压缩存储，然后用的时候再解压，虽然处理时间增加，但是耗费内存大大降低！
'''
import zlib
import os


def dataComDecom(data):
    data = data.encode()   #data为s 为bytes类型字符串对象，需要转换成str类型字符串
    print('data原始字符串长度为%d'%(len(data)))
    zb_data_com = zlib.compress(data)
    print('data压缩后的字符串长度为%d'%(len(zb_data_com)))
    zb_data_decom = zlib.decompress(zb_data_com)
    return zb_data_decom

data = '2020-02-05 17:15:06,416 [HttpRun0] INFO  RestAPI - handleGetZoneDomain result:NoError2020-02-05 17:15:06,416 [HttpRun0] INFO  RestAPI - handleGetZoneDomain result:NoError2020-02-05 17:15:06,416 [HttpRun0] INFO  RestAPI - handleGetZoneDomain result:NoError2020-02-05 17:15:06,416 [HttpRun0] INFO  RestAPI - handleGetZoneDomain result:NoError2020-02-05 17:15:06,416 [HttpRun0] INFO  RestAPI - handleGetZoneDomain result:NoError'
print(dataComDecom(data))



path = r'C:\Users\Administrator\Desktop\log搜索.txt'
with open(path,'r',encoding='UTF-8') as f:
    f_lines = f.readlines()
    for line in f_lines:
        line = line.encode()
        if line != '':
            zb_line_com = zlib.compress(line)
            print('改行被压缩后的字符串长度为%d'%(len(zb_line_com)))
            zb_line_decom = zlib.decompress(zb_line_com)
            print(zb_line_decom)
    f.close()