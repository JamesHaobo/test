# 6.改进九九乘法表，用for语句和range()函数实现。建议使用end换行。

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j),end='')
    print()