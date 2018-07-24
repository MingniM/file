# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:44:59 2018
练习题4：
1.打印每天18点的天气信息，温度，程序，情况，气压，最高温度，最低温度
2.写出英文版的天气-天气情况，用户输入英文   application应用
3.打印温度折线图
    1----------
    2--------------------
    3-------
    4----------
4.获取所有的温度，并且排序（sorted([1,4,-1,8])##########使用此方法排序）
5.友情提示，根据温度提示穿衣，打伞，出门(可选)

全球5天天气
@author: Administrator
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

#####温度，气压
#data字典-》list列表-》0 index字典-》main字典-》temp变量
data['list'][0]['main']['temp']
#data字典-》list列表-》0 index字典-》wind字典-》speed变量
data['list'][0]['wind']['speed']



sorted([1,4,-1,8])##########使用此方法排序


#练习题5
inputCity=input('please input your cit:')
url='http://api.openweathermap.org/data/2.5/forecast?q='+inputCity+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
print('______________________________________________________')

##每天18点的天气信息，温度，情况，气压，最高温度，最低温度及英文版
print('第一天18点的天气:')
print('温度(the tmp is):'+str(data['list'][2]['main']['temp']))
print('气压(the pressure is):'+str(data['list'][2]['main']['pressure']))
print('天气情况(the weather is):',data['list'][2]['weather'][0]['main'])
print('最低气温(the temp_min is):',data['list'][2]['main']['temp_min'])
print('最高气温(the temp_max is):',data['list'][2]['main']['temp_max'])
print('______________________________________________________')

print('第二天18点的天气:')
print('温度(the temp is):'+str(data['list'][10]['main']['temp']))
print('气压(the pressure is):'+str(data['list'][10]['main']['pressure']))
print('天气情况(the weather is):',data['list'][10]['weather'][0]['main'])
print('最低气温(the temp_min is):',data['list'][10]['main']['temp_min'])
print('最高气温(the temp_max is):',data['list'][10]['main']['temp_max'])
print('______________________________________________________')

print('第三天18点的天气:')
print('温度(the temp is):'+str(data['list'][18]['main']['temp']))
print('气压(the pressure is):'+str(data['list'][18]['main']['pressure']))
print('天气情况(the weather is):',data['list'][18]['weather'][0]['main'])
print('最低气温(the temp_min is):',data['list'][18]['main']['temp_min'])
print('最高气温(the temp_max is):',data['list'][18]['main']['temp_max'])
print('______________________________________________________')

print('第四天18点的天气:')
print('温度(the temp is):'+str(data['list'][26]['main']['temp']))
print('气压(the pressure is):'+str(data['list'][26]['main']['pressure']))
print('天气情况(the weather is):',data['list'][26]['weather'][0]['main'])
print('最低气温(the temp_min is):',data['list'][26]['main']['temp_min'])
print('最高气温(the temp_max is):',data['list'][26]['main']['temp_max'])
print('______________________________________________________')

print('第五天18点的天气:')
print('温度(the temp is):'+str(data['list'][34]['main']['temp']))
print('气压(the pressure is):'+str(data['list'][34]['main']['pressure']))
print('天气情况(the weather is):',data['list'][34]['weather'][0]['main'])
print('最低气温(the temp_min is):',data['list'][34]['main']['temp_min'])
print('最高气温(the temp_max is):',data['list'][34]['main']['temp_max'])
print('______________________________________________________')

print('温度折线图如图所示（the temp chart）')
print('第一天（day one）：   ','*'*int(data['list'][2]['main']['temp']))
print('第二天（day two）：   ','*'*int(data['list'][10]['main']['temp']))
print('第三天（day three)：  ','*'*int(data['list'][18]['main']['temp']))
print('第四天（day four）：  ','*'*int(data['list'][26]['main']['temp']))
print('第五天（day five）：  ','*'*int(data['list'][34]['main']['temp']))

#获取所有的温度，并且排序
print('______________________________________________________')
a=data['list'][2]['main']['temp']
b=data['list'][10]['main']['temp']
c=data['list'][18]['main']['temp']
d=data['list'][26]['main']['temp']
e=data['list'][34]['main']['temp']
print('所有温度获取及排序如下（the sorted of the temp are:）:')
print(sorted([a,b,c,d,e]))

#练习题5
inputCity=input('please input your cit:')
url='http://api.openweathermap.org/data/2.5/forecast?q='+inputCity+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
print('______________________________________________________')

##每天18点的天气信息，温度，情况，气压，最高温度，最低温度及英文版
def day(m,i):
    print('第'+str(i)+'天18:00的天气情况')
    print('温度(the tmp is):'+str(data['list'][i]['main']['temp']))
    print('气压(the pressure is):'+str(data['list'][i]['main']['pressure']))
    print('天气情况(the weather is):'+str(data['list'][i]['weather'][0]['main']))
    print('最低气温(the temp_min is):'+str(data['list'][i]['main']['temp_min']))
    print('最高气温(the temp_max is):'+str(data['list'][i]['main']['temp_max']))
print('______________________________________________________')
day(2,1)
day(10,2)
day(18,3)
day(26,4)
day(34,5)
print('______________________________________________________')

def chart(k,l):
    print('day'+str(l)+'*'*int(data['list'][l]['main']['temp']))
print('温度折线图如图所示（the temp chart）')
chart(2,1)
chart(10,2)
chart(18,3)
chart(26,4)
chart(34,5)
#获取所有的温度，并且排序
def chart(o):
    g=[data['list'][o]['main']['temp']]
    return g
f1=chart(2)
f2=chart(10)
f3=chart(18)
f4=chart(26)
f5=chart(34)
sl=[f1,f2,f3,f4,f5]
print('五天天气温度升序排序')
print(sorted(sl))

#多选其一
def day(a,i):
    print('______________________________________________________')
    print('第'+str(i)+'天18:00的天气情况')
    print('温度(the tmp is):'+str(data['list'][i]['main']['temp']))
    print('气压(the pressure is):'+str(data['list'][i]['main']['pressure']))
    print('天气情况(the weather is):'+str(data['list'][i]['weather'][0]['main']))
    print('最低气温(the temp_min is):'+str(data['list'][i]['main']['temp_min']))
    print('最高气温(the temp_max is):'+str(data['list'][i]['main']['temp_max']))
    a=str(data['list'][i]['weather'][0]['main'])
    if a=='Clear':
        print('温馨提示：时光正好，太阳正晴，去看看诗与远方吧')
    elif a=='Clouds':
        print('温馨提示：阴天多云，凉爽的同时注意不要着凉了哦')
    elif a=='Rain':
        print('温馨提示：下雨天，巧克力和音乐更配哦')
day(2,1)
day(10,2)
day(18,3)
day(26,4)
day(34,5)


  
