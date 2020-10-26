# def primeNUM(min,max):
#     if min==1:
#         print('')
#         min += 1
#     for i in range(min, max+1):
#         for j in range(2, i + 1):
#             if i % j == 0:          #判断i能不能被整除
#                 break               #退出for循环
#         if j == i:                  #若j等于i，说明i是素数
#             print(i,end=" ")
#     print('')
# primeNUM(1,10)
# 1. 编写输出10以内素数的循环程序。
for i in range(2,10):
    for j in range(2,i+1):
        if i%j==0:
            break;
    if j == i :
        print(str(i)+" 是素数")
    else:
        print(str(i)+" 等于 "+str(j)+"*"+str(int(i/j)))