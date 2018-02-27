# -*- coding:utf-8 -*-
import requests
import re
import urllib
import urllib2
from bs4 import BeautifulSoup
import codecs
# headers
User_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/54.0'
headers = {'User-agent':User_agent}

'''
url = "http://www.baidu.com"
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
print(response.read())
'''

baseURL = "https://www.baidu.com/s?"

keywords_path = "/home/manyue/Project/Git/Spider/Baidu/keywords/keywords.txt" 
link_path = "/home/manyue/Project/Git/Spider/Baidu/keywords/get_link.txt"
text_path = "/home/manyue/Project/Git/Spider/Baidu/keywords/get_text.txt"

with open(keywords_path,'r') as f:
	for word in f:
		data = {'ie':'utf-8','tn':'baiduurt','wd':word}
		searchURL = baseURL + urllib.urlencode(data)

		try:
			request = urllib2.Request(searchURL,headers=headers)
			response = urllib2.urlopen(request)
			read_response = response.read()
			soup = BeautifulSoup(read_response,"html.parser")
			all_link = soup.find_all(attrs={'class':'result c-container '})

			for link in all_link:
				with open(link_path,'a') as f_w:
					f_w.write(link.a['href'] + '\n')	

		except Exception as e:
			pass

with open(link_path,'r') as f:


		string = 'article' + '\n'
		try:
		
			for link in f:
				
				request = urllib2.Request(link,headers=headers)
				response = urllib2.urlopen(request)
				read_response = response.read()
				soup = BeautifulSoup(read_response,"html.parser")
				#print(link)
				try:
				#	find_text = soup.find('article',attrs={'class':'article'})
					content = soup.find_all('p')
				
					for t in content:
						cont = t.text
						string = string + cont.encode('utf-8') + '\n'
				except Exception as e:
					print(link)
					pass
				#print('done')
		except Exception as e:
			print(link)
			pass

  		with codecs.open(text_path, 'wb') as file:
  			file.write(string)
  			file.close()

  			
		

	


	
