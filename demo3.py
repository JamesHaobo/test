#3.用if语句判断输入的一个数字是奇数还是偶数。
#  Python判断奇数偶数
# 如果是偶数，除以2后余数为0
# 如果是余数，除以2后余数为1
n = int(input("输入一个数字:"))
if n%2 == 0:
    print(str(n)+"是偶数")
elif n%2==1:
    print(str(n)+"是奇数")
else:
    print("请正确输入一个数字")