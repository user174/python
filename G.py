s = 0
d = 0
import random
import time

print("海龍之超級無敵霹靂宇宙神奇猜個數字吧九千九百九十九分之一2.1版")
print("  ")
time.sleep(2)
print("勇敢的挑戰者,靈活的運用你的機智,你的運氣,還有你的人品來打敗我吧!")
time.sleep(2)
print("主腦生成數字中...")
time.sleep(2)
print(" ")
print("開始吧")
print(" ")
print(" ")
a = random.randint(1,9999)
while (s != a) :
    try:
        print(" ")
        s = int(input("猜個數字吧"))
        d = d + 1
        if (s > a) :
            print("你太躁進了!放慢你的腳步!")
        if (s < a) :
            print("不知進取!加快你的腳步吧!")
        if (s == a ) :
            print(" ")
            print("啊~~~~~")
            print("總共猜了",d,"次")
            print("登登登登登登,嘿~")
            print("\nWinner!"*10)
    except (TypeError,ValueError,NameError) :
        print("  ")
        print("別整我")
        continue
        



















    
