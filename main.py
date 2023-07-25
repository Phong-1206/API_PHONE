#CODER : TRAN TUAN PHONG | DEV.TTP
#CODER : TRAN TUAN PHONG | DEV.TTP
#CODER : TRAN TUAN PHONG | DEV.TTP
import requests
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
      "Sec-Fetch-Site": "same-site",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
  def Mocha(self):
    self.headers.update({"Connection": "keep-alive","Host":"apivideo.mocha.com.vn","Origin":"https://video.mocha.com.vn","Referer":"https://video.mocha.com.vn/","Content-Length":"0"})
    headers= self.headers
    textmocha = requests.post("https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp?msisdn=0334304657&languageCode=vi", headers=headers).text
    print(textmocha)
  def Winmart(self):
    phone = self.phone
    self.headers.update({"Access-Control-Request-Method": "GET","Origin":"https://winmart.vn","Referer":"https://winmart.vn/"})
    headers = self.headers
    requests.options(f"https://api-crownx.winmart.vn/cs/api/winlife/check-profile?phoneNo={phone}&identifyCardId=undefined",headers=headers).text
    requests.get(f"https://api-crownx.winmart.vn/cs/api/winlife/check-profile?phoneNo={phone}&identifyCardId=undefined",headers=headers).text
    requests.options(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=headers).text
    check=requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=headers).text
    print("Check 1: "+check)
  def The_Gioi_Di_Dong(self):
    phone = self.phone
    self.headers.update({"Origin":"https://www.thegioididong.com","Referer":"https://www.thegioididong.com/lich-su-mua-hang/dang-nhap","Content-Length":"234","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"_fbp=fb.1.1684232440829.1555200101; _tt_enable_cookie=1; _ttp=ypEGlC28gu5qy9EQYnAVt5RqOHi; _pk_id.7.8f7e=ffccac49f6b8b15b.1688043532.; amp_6e403e=PqTA5A-XdzmGBZswc_L81z...1h4e5cth9.1h4e5hqj1.0.9.9; X-CSRF-TOKEN-OurAppName=CfDJ8J9HGBxmCI9EnCi62NjpckrGt86ZVnrjKShX1sOuPnzYG4ocMo3FdplnsOrMQpQ8LxeQhX5yNWjFcj-4gdMsvL1-zaLFxThWje1Nj87_dEzqZM5M7XAZPrVcmIywfnH4wOG3_WVdeKfyET_jt41nnfA; _gid=GA1.2.1676014579.1690292888; _gat_UA-918185-25=1; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1690292899%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.7.8f7e=1; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJdJEVghENJXgOD9cjiTnF7fLxaAgys4SScJOp.1; cebs=1; _ce.s=v~259e9b29cc9acb32368cabac205216b2501d1da8~lcw~1688397575930~vpv~4~lcw~1690292899474; _ce.clock_event=1; _ce.clock_data=-333%2C171.232.212.23%2C1%2C14d58a1ba286f087d9736249ec785314; DMX_Personal=%7B%22UID%22%3A%228f0f3e1ca9152ab9dccca01118ea30cd25c2ff9d%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8Btx1b7t0ERJkQbRPSImfvI6z7DLeQlNmjrBsRvbDPKLN4myIT942ifPNzst7rz9cfsrPwYXhOEE-aaSe_i9F7Qx5HiAo6wDdJWjdRDjRPVNyCGlBmjj32KOkUFdNXFQ6rcBWFMi475u9MlUPELcPCI; _gat=1; _ga_TLRZMSX5ME=GS1.1.1690292887.7.1.1690292903.44.0.0; _ga=GA1.1.1164325889.1684232440; cebsp_=2; lhc_per=vid|a7538091b72feaf7b273; SvID=beline2687|ZL/Ss|ZL/Sm","X-Requested-With":"XMLHttpRequest"})
    headers = self.headers
    data = {
      "phoneNumber": "0334304658",
      "isReSend": "false",
      "sendOTPType": "1",
      "__RequestVerificationToken": "CfDJ8Btx1b7t0ERJkQbRPSImfvIbRnoIznOLnzBB1r9idMFm72KxhKUNzpJEoForN-fGFwDg40WjjUHt4AD0849iAQRdkySHP3_9gmI5dWWz9THcZMKUPEVcBeP9bhSc5DfAwvRTXyQPrSJSfDpNsv4FZDY"
    }
    check = requests.post("https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode",headers=headers,data=data).text
    print("Check "+check)
Api("0334304657").The_Gioi_Di_Dong()

