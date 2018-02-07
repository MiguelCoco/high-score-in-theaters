import json
import requests as rs

#豆瓣电影正在热映URL
url = 'https://api.douban.com/v2/movie/in_theaters'

#设置请求参数，城市，计数
params = {
	'city':'北京',
	'count':'100',
	}
#方法get()请求API，方法json()解析结果	
result = rs.get(url,params).json()
total = result['total']
print('正在上映电影总数： ' + str(total))
#创建存储title和score的空列表
in_theaters = []

#提取title及score，方法append()添加title及score到in_theaters列表
for i in range(total):
	title = result['subjects'][i]['title']
	score = result['subjects'][i]['rating']['average']
	genres = result['subjects'][i]['genres']
	name = result['subjects'][i]['casts'][0]['name']
	in_theaters.append((title,score,genres,name))
	#按电影分数从高到底排序
	in_theaters.sort(key=lambda score:score[1],reverse=True)
#热映电影总数写入文件
with open('in_theaters_movie.txt','a') as of:
	of.write('正在上映电影总数: {}'.format(total)) 
#提取title及score，追加写入文件
for title,score,genres,name in in_theaters:
	print(title + '： ' + str(score) + '\n\t体裁： ' + str(genres) +'\n\t主演： ' + name)


