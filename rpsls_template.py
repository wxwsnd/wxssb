#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：赵晓东
日期：5月12日
"""

import random

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":return 0
    elif name=="史波克":return 1
    elif name=="纸":return 2
    elif name=="蜥蜴":return 3
    elif name=="剪刀":return 4
    else:
        return 10

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:return"石头"
    elif number==1:return "史波克"
    elif number==2:return "纸"
    elif number==3:return "蜥蜴"
    elif number==4:return "剪刀"
    else:
        print("Error: No Correct Name")

def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    print("----------------")
    print("你的选择为：",player_choice)
    player_choice_number=name_to_number(player_choice)
    if player_choice_number==10:
        print("Error: No Correct Name")
        return player_choice_number
    import random
    comp_number=random.randrange(0,5,1)
    comp_choice_number=number_to_name(comp_number)
    print("计算机的选择为：",comp_choice_number)
    difference = (player_choice_number - comp_number) % 5
    if difference==1or 2:
            print("你赢了！")
    elif difference==3or 4:
             print("机器赢了")
    elif difference==0:
        print("平局")

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
player_choice=input()
rpsls(player_choice)


