
#           一共有多少人选课
w = ['小明','小张','小黄','小杨']
s = ['小黄','小李','小王','小杨','小周']
y = ['小杨','小张','小吴','小冯','小周']

a = w + s + y

count = 0
#排重
for o,p  in  enumerate(a):# 0,1
    if p in a[:o]:
        continue
    else:
        count = count + 1
print("一共",count,"人")
print("-----------------------------------")
#    求只选了第一个学科的人的数量和对应的名字
w = ['小明','小张','小黄','小杨']
s = ['小黄','小李','小王','小杨','小周']
y = ['小杨','小张','小吴','小冯','小周']

a = w + s + y

a=0
y=0
while a<len(w):
    print("学第一门课的同学有：",w[a])
    a=a+1
    y=y+1
print("一共有",y,"人学习第一门课")
print("-----------------------------------")
#   求只选了一门学科的学生的数量和对应的名字
p = ['小明','小张','小黄','小杨']
o = ['小黄','小李','小王','小杨','小周']
m = ['小杨','小张','小吴','小冯','小周']

t = p + o + m


i = 0
while i < len(t):
    count = 0
    # 排重
    k = 0
    flag = 0
    while k < i:
        if t[i] == t[k]:
            flag = 1
            break
        k = k + 1
    if flag == 1:
        i = i + 1
        continue # 终止后面的程序，直接进行下一轮
    # 统计
    j = i
    while j < len(t):
        if t[i] == t[j]:
            count = count + 1
        j = j + 1

    if count == 1:
        print("只学一门课的学生有",t[i])
    i = i + 1
print("-----------------------------------")
#      求只选了语文和英语的学生的数量和对应的名字
w = ['小明','小张','小黄','小杨']
s = ['小黄','小李','小王','小杨','小周']
y = ['小杨','小张','小吴','小冯','小周']

a = w + s + y

a=0
h=0
while a<len(w):
    print("学语文：",w[a])
    a=a+1
    h=h+1
print("学语文有",h,"人")

a=0
f=0
while a<len(y):
    print("英语：",y[a])
    a=a+1
    f=f+1
print("学英语有",f,"人")

print("一共有",h+f,"人")
print("-----------------------------------")
#    倒乘法
i = 9
j = 1
o = 0
while i > 0:
    if j <= i:
        print(j,"X",i,"=",(j*i),end="   ")
        j = j + 1
    else:
        print()
        j = 1
        i = i - 1
