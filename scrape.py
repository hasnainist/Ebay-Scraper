import requests
from bs4 import BeautifulSoup
import os
from PIL import Image


#paste URL here from where you want to grab ads
print('')
url=input("Enter the url :")
#url='https://www.ebay.com/itm/155285732754?epid=9054548920&hash=item2427c03d92%3Ag%3A6JcAAOSwHDxjiNmX&amdata=enc%3AAQAHAAAAoG4tXD5Q%2FxRElym%2FAAsUNScrEswqSxs3HrIhPIQTf%2FlK4kQz7vor1yVwvybJFtX1N8P6rcUaoJRMtyT3oFjAyGIzc7jTZGGoA4pGZa0ehhBjIAKFgkLaokjeR6L%2FqKPlBh42TXDSxXXXV9UHK4j6L9NAF4UYDmjJGZDw1BzY6Y681UqPvVkh1QnG4%2Bfl5%2BHqF952lWzO0vwpDkyUTrlsptk%3D%7Ctkp%3ABk9SR7LI8M6uYQ&LH_BIN=1&LH_ItemCondition=1000'   
url=str(url)
r=requests.get(url) 
htmlcontent=r.text
soup=BeautifulSoup(htmlcontent,'html.parser')
  
#getting information ad

images=soup.find("div",class_='ux-image-filmstrip-carousel')
img=images.find_all('img')
title=soup.find('h1',class_='x-item-title__mainTitle')
price=soup.find("div",class_='x-price-primary')
description=soup.find("div",class_='d-item-condition-value')
val=description.find('span',class_='clipped')
    
#printing information..you can do anything from the information obtained, here.
strTitle='Title: '+title.get_text()
strPrice='Price: '+price.get_text()
strDescription='Description: '+val.get_text()



#creating folder with title name of the ad
current_directory = os.getcwd()
final_directory = os.path.join(current_directory,title.get_text())


if not os.path.exists(final_directory):
   os.makedirs(final_directory)
   os.chdir(title.get_text())
   var=1
   for i in img:
    img_url = i.get('src')
    response = requests.get(img_url)
    if response.status_code:
     fp = open(str(var)+'.jpg', 'wb')
     fp.write(response.content)
    var=var+1

   file1 = open("info.txt", "w")
   L = [strTitle+'\n', strPrice+'\n', strDescription+'\n']
   file1.writelines(L)
   file1.close()

else:
    print('Folder of this ad already exists')


