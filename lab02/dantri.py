from urllib.request import urlopen
import urllib.request  
from bs4 import BeautifulSoup
import pyexcel

# 1. Download web page
url = "http://dantri.com.vn"

# # 1.1 Create connection
# conn = urlopen(url)

# # 1.2 Read
# data = conn.read()

# # 1.3 decode
# html_content = data.decode('utf-8')


## cach khac
html_content = urlopen(url).read().decode('utf-8')
# print(html_content)

# save html to file
# f = open('dantri.html','wb')
# f.write(html_content)
# f.close()


# urllib.request.urlretrieve("http://dantri.com.vn", "dantri.html")

# 2. Extract ROI (Region of interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, 'html.parser')
# find by class
ul = soup.find('ul', 'ul1 ulnew')
# print(ul.prettify())

# 3. Extract data
li_list = ul.find_all('li')
dictionary=[]

for li in li_list:
    # li = li_list[i]
    # print(li.prettify())
    a = li.h4.a 
    # print(a)
    # print(a.string)
    # print(url + a['href'])
    # print("* "*30)
    dic={}
    dic['title'] = a.string
    dic['link'] = url + a['href']
    dictionary.append(dic)
    


pyexcel.save_as(records=dictionary, dest_file_name="dantri.xlsx")


