#自保2班  赵晓东 运用自定义函数判断两个数区间是否有交集
def interval_intersect():
    int1_lower=float(input("输入函数下限"))
    int1_upper=float(input("输入函数上限"))
    int2_lower=float(input("输入函数下限"))
    int2_upper=float(input("输入函数上限"))
    if int1_lower>int2_upper or int1_upper<int2_lower:
       print("无交集")
    else:
       print("两个区间有交集")
interval_intersect()
