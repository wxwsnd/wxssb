#自保2班 赵晓东 45调用自定义函数计算变量的值
def function_caculation():
    x=eval(input("输入函数值"))   #获取返回值函数
    y=0
    if x>3:y=2*x-10  #使用if语句来表达定义域
    elif x<-3:y=5*x-2
    else:
        y=x+9
    print("结果为:",y)
function_caculation()

