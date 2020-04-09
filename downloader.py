import requests
import os
from bs4 import BeautifulSoup

def image_download(url,name):
	response=requests.get(url).text
	soup=BeautifulSoup(response,"html.parser")
	myimages=soup.findAll("a")
	links=[]
	for image in myimages:
		if image.img:
			a=image.img["src"]
			if a[0]=="h":
				links.append(a)
	i=0
	os.mkdir(name)
	os.chdir(name)
	for link in links:
		a=name
		a=a+str(i)
		f=open(a+".jpg","wb")
		image_file=requests.get(link)
		f.write(image_file.content)
		f.close()
		i=i+1

print("Enter Image Name")
word=input()
url_link="https://www.google.com/search?tbm=isch&tbs=isz:lt,islt:12mp&q="+word
image_download(url_link,word)
