#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�5��12��
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":return 0
    elif name=="ʷ����":return 1
    elif name=="ֽ":return 2
    elif name=="����":return 3
    elif name=="����":return 4
    else:
        return 10

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:return"ʯͷ"
    elif number==1:return "ʷ����"
    elif number==2:return "ֽ"
    elif number==3:return "����"
    elif number==4:return "����"
    else:
        print("Error: No Correct Name")

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("----------------")
    print("���ѡ��Ϊ��",player_choice)
    player_choice_number=name_to_number(player_choice)
    if player_choice_number==10:
        print("Error: No Correct Name")
        return player_choice_number
    import random
    comp_number=random.randrange(0,5,1)
    comp_choice_number=number_to_name(comp_number)
    print("�������ѡ��Ϊ��",comp_choice_number)
    difference = (player_choice_number - comp_number) % 5
    if difference==1or 2:
            print("��Ӯ�ˣ�")
    elif difference==3or 4:
             print("����Ӯ��")
    elif difference==0:
        print("ƽ��")

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()
rpsls(player_choice)


