import requests
from bs4 import BeautifulSoup
print("SJC22MCA-2027 : Georgekutty Biju\nS3MCA")
def getdata(url):
    r=requests.get(url)
    return r.content
htmldata = getdata("https://sjcetpalai.ac.in/")
#htmldata = getdata("https://sjcetpalai.ac.in/")
soup = BeautifulSoup(htmldata,'html.parser')
links = soup.find_all("a")
print("links:",len(links))
for link in links:
    if link.get("href") != "":
        print("Link:",link.get("href"),"Text", link.string)