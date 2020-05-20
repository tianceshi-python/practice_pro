# encoding:utf-8
"""
通过学习的python知识，写一个简单的python小游戏
游戏名字：掷骰子比大小
游戏规则：
1、玩家可以选择玩掷几个骰子游戏（默认3个）
2、玩家可以设置双方初始的游戏金额（默认10）
3、玩家可以设置每次投入金额（默认1）
4、通过比大小决定比赛胜负
5、一方金额归0则游戏结束
"""

import random

# 首先让玩家通过输入的方式将游戏规则设置好，也可以让其不设置，直接使用默认条件开始游戏
def setRule():
    #设置玩骰子游戏的个数
    istoSet = input('是否开始设置游戏相关规则：（输入‘是’则进入设置，其他则使用默认）')
    game_Num = 3
    gameinit_money = 10
    one_Game = 1
    if istoSet == '是':
        # 让玩家设置使用几个骰子游戏
        game_Num = input('请设置骰子个数，设置的值必须是大于0的数字，输入其他则使用默认值')
        if game_Num.isdigit():    #isdigit() 方法检测字符串是否只由数字组成。
            if int(game_Num) > 0:
                game_Num = int(game_Num)
        #让玩家设置游戏的初始金额
        gameinit_money = input('请设置初始游戏金额，设置值必须是大于0的数字，输入其他则使用默认值')
        if gameinit_money.isdigit():
                if int(gameinit_money) > 0:
                    gameinit_money = int(gameinit_money)
        #让玩家设置每次投入金额
        one_Game = input('请设置每次投入的金额，设置值必须是大于0且小于初始金额的数字，输入其他则使用默认值')
        if one_Game.isdigit():
            if int(one_Game) > 0 and int(one_Game) < gameinit_money:
                one_Game = int(one_Game)

    else:
        print('恭喜您设置完成')

    data = [game_Num,gameinit_money,one_Game]
    print('您的设置值是：',data)
    return data

#通过比较大小决定游戏胜负，如果一方金额归0则游戏结束，判断输赢
def meGame():
    data = setRule()      #获取游戏设置的设置值（骰子个数、玩家的初始金额、玩家每次投入金额）
    game_Num = data[0]     #骰子个数
    gameinit_money1 = data[1]    #玩家的初始金额
    gameinit_money2 = data[1]    #AI的初始金额
    one_Game = data[2]           #玩家每次投入金额
    print(str(game_Num) + '个骰子比大小')
    while gameinit_money1 > 0 and gameinit_money2 > 0:     #如果一方金额归0则游戏结束，判断输赢
        print('您目前的资产是：',gameinit_money1,'AI目前的资产是：',gameinit_money2)
        choice = ['大','小']
        user_choice = input('买大买小，买定离手:')
        number = game_Num
        if user_choice in choice:
            points = []        #记录所有骰子的点数
            biggist = game_Num*6
            smallest = game_Num
            data =get_medium(smallest,biggist)     #获取中间数字，用于判断点数是大是小
            print(data)
            while number > 0:         #当骰子个数大于0时；
                point = random.randrange(1,7)      #点数时1到7之间的任意值
                points.append(point)
                number = number - 1
            total = sum(points)      #所有骰子的点数之和
            big = data[0] <= total <= biggist     #确定骰子点数是大
            small = smallest <= total <= data[1]    #确定骰子点数是大
            win = (big and user_choice == '大') or (small and user_choice == '小')
            if win:
                print('点数是：' + str(total) + '你赢啦！，资产要增加了哦！')
                gameinit_money1 = gameinit_money1 + one_Game
                gameinit_money2 = gameinit_money1 - one_Game
            else:
                print('点数是：' + str(total) + '你输啦！哦哦您的资产又减少了！！')
                gameinit_money1 = gameinit_money1 - one_Game
                gameinit_money2 = gameinit_money1 + one_Game


        else:
            print('请输入‘大’或‘小’')


    else:
        if gameinit_money1 < 0:    #玩家的初始金额小于0，则玩家输
            print('抱歉您输啦！')
        else:
            print('您赢啦！6666')


#获取中间数字
def get_medium(num1,num2):
    data = []
    while num1 <= num2:
        data.append(num1)
        num1 = num1 + 1
    #print(data)
    data.sort()
    half = len(data)//2    #获取骰子点数从最小到最大的中间位置
    #lists[0]是中间数偏大，lists【1】是中间数偏小，用于划分骰子点数是属于大，还是属于小
    lists = [data[half],data[~half]]
    return lists

if __name__ == '__main__':
    meGame()




