# 7. 求指定区间内的水仙花数（亦称阿姆斯特朗数），要求使用循环语句和判断语句。
# 如果一个n位正整数等于其各位数字的n次方之和，则称该数为水仙花数或阿姆斯特朗数。例如3^3 + 7^3 + 0^3 = 370。
# 1000以内的水仙花数有： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
min=int(input("请输入最小值: "))
max=int(input("请输入最大值: "))
for i in range(min,max):
    bai = i // 100
    shi,ge=(i-bai*100)//10,i%10
    if i==ge**len(str(i))+shi**len(str(i))+bai**len(str(i)) :
        print("{}".format(i),end=",")