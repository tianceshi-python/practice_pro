# encoding:utf-8
'''
主要功能：
1、在规定的时间内集齐五福则成功；
2、一张万能福可以代替任何一张'友善','敬业','富强','和谐','爱国'福字；
3、集福的时候获得‘全家’福，则恭喜玩家。
'''
import time

def setF():
    list = ['友善','敬业','富强','和谐','爱国','万能','全家']
    result = []
    ticks = time.time()
    family_flg = 0
    while ticks > 1588176000:     #在规定的时间内完成集福
        #print(list)
        str = input('请输入您收集的福字：\n')
        str.encode('utf-8')
        for i in list:
            if i == str and ((' '.join(result)).find(i) == -1) :    #判断输入的字符串是不是在福字列表中，并且结果列表中没有这个字符串
                if i != list[-1]:    #如果集的福不是全家福，则将福字计入结果列表
                    result.append(str)
                else:
                    family_flg = 1

        if len(result) == 5:      #如果五福集全，则跳出循环
            break
        ticks = time.time()

    print('集福结束！！')
    return result,family_flg




if __name__ == '__main__':
    result_list,flag = setF()
    print(result_list)
    print(flag)
    if len(result_list) == 5 :
        print('恭喜集福成功，坐等开奖哦！！！')
    else:
        print('很遗憾没有集全，明年继续努力！！！')
    if flag == 1:
        print('恭喜获取全家福哦！！')
    else:
        print('很遗憾没有获得全家福！！！')