# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:38:36 2018

@author: liumingmin
"""
ls=open('all_school.txt',encoding='utf-8').readlines()
schoolls=[]

for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}

f=open('辽宁高考文科招生统计.txt','a',encoding='utf-8')
for schoolid in schoolls[0:2300]:
    req=r.Request(url,data='id={}&type=1&city=21&state=1'.format(schoolid).encode(),headers=headers)
    f.write(r.urlopen(req).read().decode('utf-8','ignore')+"\n")
f.close()



ls=open('all_school.txt',encoding='utf-8').readlines()
print('学校编号为：\n')
for i in range(0,2300):
    print(ls[i].split('-jianjie-')[1].split('.')[0])



ls1=open('XML高考派城市.txt',encoding='gbk').readlines()
print('招生城市编号为：\n')
for n in range(1,32):  
    print(ls1[n].split('<li data-val=')[1].split('data-id')[0]+':'+ls1[n].split('claimCity')[1].split(')">')[0])
    
    
ls=open('ning.txt',encoding='utf-8').readlines()
for i in range(2,5):
    print(ls[i].split('-jianjie-')[1].split('.')[0])  


f=open('ning.txt',encoding='utf-8').readlines()
ls=[]
data=[]
for line in f:
    ls.append(str(line.split('(')[1].split(',')[0]))
    data.append(int(line.split(',')[1].split(')')[0]))
    print(ls)
    print(data)


    
ls=open('ning.txt',encoding="utf-8").readlinesk()
for line in ls[1:-1]:
    min=line.split(",")[1].split(")")[0]
    num=line.split("\">")[1].split
    
    
    
    
    
    
    
    
    
    
    
    
    

