import requests
import sys


param = {'username':'mg1533071','password':'625106'}
r = requests.post('http://p.nju.edu.cn/portal_io/login',data = param)
#print sys.getefaultencoding()
print r.content,type(r.content)

"""
tmp_value = 'SPD20150575'
path = 'HYPERLINK("file:///C:\\Users\\wushuang\\Desktop\\baby\\mk watch I\\' + \
        str(3+1) + "\\" + '";"' + str(tmp_value) +'")'

print path

"""