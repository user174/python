
import easygui
z=0
x=0
c=0
f = easygui.msgbox("翻譯麵-----90\n算陪麵-----110\n奶雞麵-----120\n青蛤麵-----150","海龍餐館  菜單","點餐")
a = easygui.choicebox("菜單(主菜)",choices=["翻譯麵","算陪麵","奶雞麵","青蛤麵"])
print(a)
g = easygui.msgbox("幾度夕陽紅茶------------25\n有何不可樂--------------30\n陽春白雪碧--------------30\n無心插柳柳橙汁----------40","海龍餐館  菜單","點餐")
s = easygui.choicebox("菜單(飲品)",choices=["幾度夕陽紅茶","有何不可樂","陽春白雪碧","無心插柳柳橙汁"])
print(s)
d = easygui.choicebox("飲品加大與否(+5元)",choices=["加大","鼻要"])
if d == "加大":
    c=5
    print("\n跟您確認尼的餐點:\n主餐"+a+",飲品"+s+"加大")
if d == "鼻要":
    print("\n跟您確認尼的餐點:\n主餐"+a+",飲品"+s)
if a == "翻譯麵":
    z = 90
if a == "算陪麵":
    z = 110
if a == "奶雞麵":
    z = 120
if a == "青蛤麵":
    z = 150
if s == "幾度夕陽紅茶":
    x = 25
if s == "有何不可樂":
    x = 30
if s == "陽春白雪碧":
    x = 30
if s == "無心插柳柳橙汁":
    x = 40
v=z+x+c
b=str(v)
print("總共是"+b+"元")
n=str(z)
m=str(x)

if d == "加大":
    easygui.msgbox(a+"---"+n+"\n"+s+"---"+m+"飲品加大---5\n總共"+b+"元","帳單","結帳")
if d == "鼻要":
    easygui.msgbox(a+"---"+n+"\n"+s+"---"+m+"\n總共"+b+"元","帳單","結帳")






