#coding=utf-8
from lib import wmiexec
import re
try:
    ps=wmiexec.WMIEXEC(command='cmd',username='administrator',password='1')
    result=ps.run('192.168.6.130')
    if result:
        print "login ok"
except Exception,e:
    msg=str(e)
    if re.search('.*STATUS_LOGON_FAILURE',msg):
        print 'login fail'

