### 文章内容不能写到文件里？
编码的问题 unicode -> unicode.encode('utf-8') 
```
string = ''
soup = BeautifulSoup(read_response,"html.parser")
content = soup.find_all('p')
for t in content:
	cont = t.text
	string = string + cont.encode('utf-8') + '\n'
```
### 不是所有的文章都写在'article'标签里?
直接搜索<p>标签里的内容，不要用<article>
```
delete # 	find_text = soup.find('article',attrs={'class':'article'})
```
但获得的text中会有乱码/代码行？
