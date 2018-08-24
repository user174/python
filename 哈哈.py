import requests
s = 0
while s==0 :
    a = "http://www.jwsh.tp.edu.tw/bin/home.php"
    resp = requests.get(a)
    print(resp)
