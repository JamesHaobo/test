# 2.使用if-elif-else语句判断输入的数字是正数、负数还是零。使用嵌套的if语句实现同样的功能。
n  = input("请输入一个数字:")
num = int(n)
if num>0:
    print("正数")
elif num==0:
    print("零")
else:
    print("负数")

