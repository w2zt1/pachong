from urllib.request import urlopen
html = urlopen("https://blog.yuantongblog.cn/archives/29.html").read().decode("utf-8")
print(html)