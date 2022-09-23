import requests,time,socket,re

UserName='17*******35'
pwd=[
        "b74173ecb70acdd9",
        "c285e72bcf0588a5",
        "ddece0ddc51df519",
        "ef5de658c563a4bf",
        "c48e163e095938e7",
        "9daaa7de33a8b581",
        "6e3a0af029b8859b",
        "d1eaed0fcd4b4114",
        "8194d9d30f51dcfe",
        "378dceb0009886e8",
        "fba53519389e86ad",
        "1a1be2ad357ebde6",
        "3ed5df8ef565dd61",
        "c6d167033330f2fa",
        "8875cb6ec680280c",
        "f2544e3272d604f3",
        "d835ad69d84aaa72",
        "b148d1f3c340301d",
        "65aa8c6e832c29a9",
        "12c4af27aea553e8",
        "7ed43a12ae1fda89",
        "e26ffe523751817f",
        "f2f40b2db653cf1b",
        "bd414088b25a7a2e",
        "00ede862fdbea028",
        "6d50195c46fe4491",
        "367db3a9a72ea6af",
        "a0c00a21fde8940f",
        "18a26c64ed55c5d5",
        "21fe1121bd0cc2c5",
        "1ba6b7e0bb2aae4c"
]


UserHard1='!^Iqnd0'
UserHard2='!^Adcm0'
NowTime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#20220222
dateDay=NowTime[6:8]
print("号数:"+dateDay)
# UserMAC='b0-70-2d-de-d1-3a'
# print("UserMac:",UserMAC)
Password=pwd[int(dateDay)-1]

#获取计算机名称
hostname=socket.gethostname()
#获取本机IP
Userip=socket.gethostbyname(hostname)

redictUrl='http://www.msftconnecttest.com/redirect'
redictUrl="http://100.64.0.1"
#redictUrl="http://58.53.199.144:8001/?"

response1=requests.get(redictUrl,timeout=1)
# print(response1.text)
# print(response1.headers)
print(response1.history)
red=response1.history
gotUrl=red[0].headers['Location'] #得到的url,取其ip
print(gotUrl)
gotUrl=str(gotUrl)
Userip_ex=".*?userip=(.*?)&wlanacname.*?"
Userip=re.findall(Userip_ex,gotUrl,re.S)[0]
print("路由ip:"+Userip)
# if(Userip[:6]!='100.64'):
# 	#Userip=input("输入路由器后两位ip:")
# 	a,b=input("输入路由器后两位ip,用空格键分开:").split(" ")
# 	Userip="100.64."+a+'.'+b
# 	#Userip="100.64."+Userip
# Userip=''
Remoteip_ex=".*?nasip=(.*?)&usermac.*?"
Remoteip=re.findall(Remoteip_ex,gotUrl)[0]
print("Remote ip:",Remoteip)
#Remoteip='59.172.216.49'

UserMAC_ex='.*?usermac=(.*)'
UserMAC=re.findall(UserMAC_ex,gotUrl)[0]
print("UserMAC:",UserMAC)
#first requests url,get sessionID
url1='http://58.53.199.144:8001/?userip='+Userip+'&wlanacname=&nasip='+Remoteip+'&usermac='+UserMAC+'&aidcauthtype=0'
url2='http://58.53.199.144:8001/wispr_auth.jsp'
Headers1={
    "User-Agent": "CDMA+WLAN(Mios)"
}
Headers2={
    "User-Agent": "CDMA+WLAN(Mios)",
    "Content-Type": "application/x-www-form-urlencoded",
}


response=requests.get(url=url1,headers=Headers1)
print(response.text)

url2_ex=".*?wispr_auth.jsp?(.*?)]].*?"
url2=url2+re.findall(url2_ex,response.text)[0]
print(url2)

url2_time_ex=".*?<AidcAuthAttr1>(.*?)</AidcAuthAttr1>"
NowTime=re.findall(url2_time_ex,response.text)[0]


data="UserName=" + UserHard2 + UserName + "&Password=" + Password + "&AidcAuthAttr1=" + NowTime +\
		"&AidcAuthAttr3=keuyGQlK&AidcAuthAttr4=zrDgXllCChyJHjwkcRwhygP0&AidcAuthAttr5=kfe1GQhXdGqOFDteego5zwP9IsNoxX7djTWspPrYm1A%3D%3D&" +\
		"AidcAuthAttr6=5Ia4cQhDfXSFbTtUDGY1yx8%3D&AidcAuthAttr7=6ZWiVlwdNiHMXCpOagQv2w2MQs0ohTWJnTu8qK5OibhCydTpTxkI88wadKPWby%2F2PKCVaZ" +\
		"UxglbBs96%2FtmLE89M8AJ6y28o7qolpFep%2FcYFFRLd7H4MAMrDUMRO0F%2B93jh14fiAZYmtk9hdp%2BZ5w%2BjMQUoV4TCtM9VJ07XQwxlMVg%2F0YKrS1s3hXA" +\
		"stdQ1fvdSn3nAVGgdxc%2BJQDrQ%3D%3D&AidcAuthAttr8=jPSyBQxVaXWTQWUaakluj06scJ98nyqCyX7y%2FLUk1OkXiNjkXhVGvJhyTuLDaCPhK%2FOFJttlxxi" +\
		"VqNKupnDXkp9%2BR9D9j8p2j5h8FOxoatMaGu0oRdk%3D&createAuthorFlag=0"
print(data)
response2=requests.post(url=url2,data=data,headers=Headers2)

print(response2)
print(response2.text)
aaa=input("input a key to exit")



