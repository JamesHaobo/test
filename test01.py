str1=input("请输入你所想要转换的温度（温度的格式是：134F、33C）\n")
try:
    flag=str1[-1]
    num1=float(str1[0:-1])
    if flag in ["F","f"]:
        print("华氏摄氏度"+str1+"转换后摄氏温度为"+str((int(num1)-32)/1.8)+"C")
    elif flag in ["C","c"] :
        print("摄氏摄氏度"+str1+"转换后华氏温度为"+str(int(num1)*1.8+32)+"F")
    else:
        print("请重新温度")
except BaseException :
    print("输入温度的数值有问题")
