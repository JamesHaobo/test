# 5.使用标准格式输出阶乘（factorial）。
# 整数的阶乘是所有小于及等于该数的正整数的积，即：n!=1×2×3×... ×n。0的阶乘定义为1。
n = int(input("请输入一个数字:"))
sum=1
for i in range(1,n+1):
    if n==0:
        break
    sum*=i
print(str(n)+"的阶乘为"+str(sum))