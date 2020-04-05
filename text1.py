from urllib import request

resp = request.urlopen('http://www.nyez.com.cn')
print(resp.read().decode())
