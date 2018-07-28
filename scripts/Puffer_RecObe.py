import urllib3

from bs4 import BeautifulSoup

http = urllib3.PoolManager()
url = 'http://192.168.2.112:8083/fhem/floorplan/Pufferspeicher'
response = http.request("GET", url)

soup = BeautifulSoup(response.data, "html.parser")
name_box = soup.find("div", attrs={"id": "recobe"})
name = name_box.text.strip()[3:5]
print(name)