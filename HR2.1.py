s=0
d=0
f=0
g=0
print("歡迎使用海龍神奇計算機2.1版")
print("教程開始\n海龍神奇計算機2.1版提供以下計算")
print("java,剪髮,懲罰,處罰,次方,根號")
print("那麼,祝您旅途愉快!")

while g==0:
    print(" ")
    s=int(input("輸入運算符號\n加法按1,減法按2,乘法按3,除法按4,次方按5,根號按6\n若要離開按0"))
    if s==1:
        d=float(input("運算式:A+B , 請輸入A"))
        f=float(input("運算式:A+B , 請輸入B"))
        print(d+f)
    if s==2:
        d=float(input("運算式:A-B , 請輸入A"))
        f=float(input("運算式:A-B , 請輸入B"))
        print(d-f)
    if s==3:
        d=float(input("運算式:AxB , 請輸入A"))
        f=float(input("運算式:AxB , 請輸入B"))
        print(d*f)
    if s==4:
        d=float(input("運算式:A/B , 請輸入A"))
        f=float(input("運算式:A/B , 請輸入B(請勿輸入0)"))
        if f==0:
            print("滾吧")
        else :print(d/f)
    if s==5:
        d=float(input("運算式:A的B次方 , 請輸入A"))
        f=float(input("運算式:A的B次方 , 請輸入B"))
        print(d**f)
    if s==6:
        d=float(input("運算式:根號A開B次 , 請輸入A"))
        f=float(input("運算式:根號A開B次 , 請輸入B"))
        print(d**(1/f))
    if s==0:
        print("   ")
        print("謝謝遊玩,一共是九千四百八十七元")
        g=12
    


    


    
