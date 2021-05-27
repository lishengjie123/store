#  之和 平均数


a1 = input("请输入第一个数字：")
a1 = int(a1)
a2 = input("请输入第二个数字：")
a2 = int(a2)
a3 = input("请输入第三个数字：")
a3 = int(a3)
a4 = input("请输入第四个数字：")
a4 = int(a4)
a5 = input("请输入第五个数字：")
a5 = int(a5)
a6 = input("请输入第六个数字：")
a6 = int(a6)
a7 = input("请输入第七个数字：")
a7 = int(a7)
a8 = input("请输入第八个数字：")
a8 = int(a8)
a9 = input("请输入第九个数字：")
a9 = int(a9)
a10 = input("请输入第十个数字：")
a10 = int(a10)

a = (a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)

print("您的数字相加结果为：",a)
print("您的数字相加平均数为：",a/10)




#  最大的数
a1 = input("请输入第一个数字：")
a1 = int(a1)
a2 = input("请输入第二个数字：")
a2 = int(a2)
a3 = input("请输入第三个数字：")
a3 = int(a3)
a4 = input("请输入第四个数字：")
a4 = int(a4)
a5 = input("请输入第五个数字：")
a5 = int(a5)
a6 = input("请输入第六个数字：")
a6 = int(a6)
a7 = input("请输入第七个数字：")
a7 = int(a7)
a8 = input("请输入第八个数字：")
a8 = int(a8)
a9 = input("请输入第九个数字：")
a9 = int(a9)
a10 = input("请输入第十个数字：")
a10 = int(a10)
if a1 > a2 and a1 > a3 and a1 > a4 and a1 > a5 and a1 > a6 and a1 > a7 and a1 > a8 and a1 > a9 and a1 > a10:
    print("您输入最大数为：",a1)
elif a2 > a1 and a2 > a3 and a2 > a4 and a2 > a5 and a2 > a6 and a2 > a7 and a2 > a8 and a2 > a9 and a2 > a10:
    print("您输入最大数为：",a2)
elif a3 > a1 and a3 > a2 and a3 > a4 and a3 > a5 and a3 > a6 and a3 > a7 and a3 > a8 and a3 > a9 and a3 > a10:
    print("您输入最大数为：",a3)
elif a4 > a1 and a4 > a2 and a4 > a3 and a4 > a5 and a4 > a6 and a4 > a7 and a4 > a8 and a4 > a9 and a4 > a10:
    print("您输入最大数为：",a4)
elif a5 > a1 and a5 > a2 and a5 > a3 and a5 > a4 and a5 > a6 and a5 > a7 and a5 > a8 and a5 > a9 and a5 > a10:
    print("您输入最大数为：",a5)
elif a6 > a1 and a6 > a2 and a6 > a3 and a6 > a4 and a6 > a5 and a6 > a7 and a6 > a8 and a6 > a9 and a6 > a10:
    print("您输入最大数为：",a6)
elif a7 > a1 and a7 > a2 and a7 > a3 and a7 > a4 and a7 > a5 and a7 > a6 and a7 > a8 and a7 > a9 and a7 > a10:
    print("您输入最大数为：",a7)
elif a8 > a1 and a8 > a2 and a8 > a3 and a8 > a4 and a8 > a5 and a8 > a6 and a8 > a7 and a8 > a9 and a8 > a10:
    print("您输入最大数为：",a8)
elif a9 > a1 and a9 > a2 and a9 > a3 and a9 > a4 and a9 > a5 and a9 > a6 and a9 > a7 and a9 > a8 and a9 > a10:
    print("您输入最大数为：",a9)
elif a10 > a1 and a10 > a2 and a10 > a3 and a10 > a4 and a10 > a5 and a10 > a6 and a10 > a7 and a10 > a8 and a10 > a9:
    print("您输入最大数为：",a10)




#  50-150之间的数










#  三角形

while True:
    a = input("请输入第一条边")
    a = int(a)
    b = input("请输入第一条边")
    b = int(b)
    c = input("请输入第一条边")
    c = int(c)
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("构成等边三角形")
            break
        elif a == b or a == c or b == c:
            print("构成等腰三角形")
            break
        elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            print("构成直角三角形")
            break
        else:
            print("构成普通三角形")
            break
    else:
        print("不构成三角形")
        break




#  三次错误密码锁定
name = "root"
password = "admin"
a = 0
while a < 3:
    a = a + 1
    b = input("请输入：")
    if b == "admin":
        print("登陆成功")
        break
    else:
        print("密码错误")




#1-100之内的和
b = 1
x = 0
while True :
    b = b + 1
    x = x + b
    if b >= 99 :
        print(x)
        break



#  青蛙
J = 0
X = 0
while J < 20:
    X = X + 1
    J = J + (3-2)
    if J >= 20:
        print("您一共爬了",X,"天")



#猜数
import random
num = random.randint(0,100)

x = 5000
while True:
    x = x - 500
    a = input("请输入您要猜的数字：")
    a = int(a)
    if a > num:
        print("大了！")
        if x < 500:
            print("-----------------")
            print("您的余额不足,请充值！")
            break
    elif a < num:
        print("小了！")
        if x < 500:
            print("-----------------")
            print("您的余额不足,请充值！")
            break
    else:
        print("恭喜您猜中了！奖励200元！您本次消费了", 5000 - x, "元,""一共猜了", ((5000 - x) / 500), "次,您的当前余额为", x + 200, "元。")
        break
