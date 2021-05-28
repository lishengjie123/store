#          5倍数的和
a = [1, 5, 21, 30, 15, 9, 30, 24]
i= 0
s= 0
num =0
while i<=7:
    i=i+1
    if  a[num] % 5 == 0:
        s = s+a[num]
        num=num+1
    else:
        num = num+1
print(s)
#           星星
q = 1
while q <= 7:
    k=7
    while k>=q:
        j = 1
        print(" ",end="")
        k=k-1
    while j<=q:
        print("* ",end="")
        j = j+1
    print()
    q = q+1
#   平均数
a = ["北京","上海","广东"]
a.append("石家庄,哈尔滨,长春,沈阳,兰州,西宁,太原,郑州,济南,合肥,武汉,长沙,南京,成都,贵阳,昆明,杭州,南昌,广州,福州,台北,海口")
a[0] = "广东"
a[2] = "北京"
print(a)


b = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
#      b = round(b,2)      保留两位小数
#print("前八城市JDP总和为：",b)

#      c = round(c,2)
#print("前八城市JDP平均值为：",c)
print("平均数为",sum(b)/len(b))

c = [1,2,3,]
print("平均数为",sum(c)/len(c))

#  统计出现的次数
import collections

a = [5,2,4,8,6,2,1,4,7,5,4,1,2,3,5,8,4,1,2]
b = collections.Counter(a)
for c in b:
    print(c,"出现",b[c],"次")

#       翻转
list = [8,2,8,4,5,8,5,8,8]
list.reverse()
print(list)


#    默认翻转成正序
a = [1,5,8,6,2,4]
a.sort()
print(a)

#    添加条件翻转成逆序
b = [5,6,1,7,8,2,3]
b.sort(reverse=True)
print(b)