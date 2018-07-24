import urllib.request as r#导入联网工具包，名为为r
import json
f=open('西安裙子数据.txt','w',encoding='utf-8')
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E8%A5%BF%E5%AE%89&bcoffset=1&p4ppushleft=1&url={}&ajax=true'
for i in range(0,100):
    url=url.format(i*44)
    data=r.urlopen(url).read().decode('utf-8','ignore')
    data=json.loads(data)
    f.write(str(data)+'\n')
    
    print('成功获取第'+str(i+1)+'页数据')
f.close

import urllib.request as r#导入联网工具包，名为为r    
f=open('西安裙子数据.txt','a',encoding='gbk') 
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E8%A5%BF%E5%AE%89&bcoffset=1&p4ppushleft=1&url={}&ajax=true'
for i in range(0,100):
    url1=url.format(i*44)
    try:
        data=r.urlopen(url1).read().decode('utf-8','ignore')
        f.write(data+'\n')
        print('成功获取第{}行数据'.format(i+1))
    except Exception as err:
        print('此行有误')
f.close()

