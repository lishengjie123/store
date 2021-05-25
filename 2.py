# T恤
number1 = 1
name1 = "T恤"
price1 = 300
amount1 = 100
size1 = "s-xxxl"
pop1 = "温州"

#牛仔裤
number2 = 2
name2 = "牛仔裤"
price2 = 1000
amount2 = 102
size2 = "s-xxxl"
pop2 = "温州2"

#卫衣
number3 = 3
name3 = "卫衣"
price3 = 800
amount3 = 103
size3 = "s-xxxl"
pop3 = "温州3"

#短裤
number4 = 4
name4 = "短裤"
price4 = 500
amount4 = 104
size4 = "s-xxxl"
pop4 = "温州4"

print("================欢迎来到李盛杰的皮革服装商城==================")
print("编号        名称       价格        数量       尺码       产地")
print("---------------------------------------------------------")
print(number1,"       ",name1,"     ",price1,"      ",amount1,"      ",size1,"     ",pop1)
print(number2,"     ",name2,"     ",price2,"     ",amount2,"      ",size2,"    ",pop2)
print(number3,"       ",name3,"     ",price3,"      ",amount3,"      ",size3,"     ",pop3)
print(number4,"       ",name4,"     ",price4,"      ",amount4,"      ",size4,"     ",pop4)

print("总金额￥:",price1 * amount1 + price2 * amount2 + price3 * amount3 + price4 * amount4)