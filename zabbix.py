'''
Created on 01.10.2010

@author: gescheit
'''
from zabbix_api import ZabbixAPI

server = "http://http://zabbix.asskickery.us"
path = "/"
username="aAdmin"
password="zabbix"

zapi = ZabbixAPI(server=server, path=path, log_level=6)
zapi.login(username, password)

host_name="use1a-pri-uidelegate-0x1x0-01"

description='Used disk space on $1 in %' 
key='vfs.fs.size[/,pused]'

hostid=zapi.host.get({"filter":{"host":host_name}})[0]["hostid"]
print hostid
#zapi.item.create({ 'hostid' : (hostid),'description' : (description),'key_' : key })