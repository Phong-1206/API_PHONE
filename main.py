#CODER : TRAN TUAN PHONG | DEV.TTP
#CODER : TRAN TUAN PHONG | DEV.TTP
import requests
class Api:
  def __init__(self):
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
  
Api().Mocha()
