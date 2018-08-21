a=0
while a != 1000:
    a=int(input("請輸入一溫度數值"))
    s=int(input("若為華氏請按1,若為攝氏請按2"))
    if s==1:
        print((a-32)*5/9,"°C")
    if s==2:
        print((9/5)*a+32,"°F")
    if s!=1 and s!=2:
        print("你他媽是要華氏還是攝氏你說清清楚啊!")

    
