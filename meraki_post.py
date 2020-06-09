# ----------------------------------------------------
# Projekt MNET3.0 Auomation - Alexander Sagarra
# Meraki Beispiel mit etwas erstellen ..
#
# ----------------------------------------------------
#    {"id":"968803","name":"MGB TEST","url":"https://n255.meraki.com/o/ECljab/manage/organization/overview"},
#    {"id":"608567","name":"MGB","url":"https://n236.meraki.com/o/tpyDmd/manage/organization/overview"}
#
#Local Client Network VLAN ID: 10
#Local Client Network IP Range: 192.168.128.0/24
#
#Lab Diagram:
#+--------------------------------------+
#|                                      |
#|                  +----------------+  |
#|                  |                |  |
#|                  |  Meraki Cloud  |  |
#|     Internet     |  Management    |  |
#|                  |                |  |
#|                  |                |  |
#|                  |                |  |
#|                  +----------------+  |
#|                                      |
#+-------+------------------------------+
#        |
#        |
#+-------+------+     +-----------------+
#|              |     |                 |
#|  MX Firewall |     | MS Switch       |
#|              +-----+                 |
#|              |     |                 |
#|              |     |                 |
#+--------------+     +--------+--------+
#                              |
#                     +--------+--------+
#                     |                 |
#                     | MR Access Point |
#                     |                 |
#                     |                 |
#                     +-----------------+
# ----------------------------------------------------

import requests 
import json
import meraki_func as f

global apiKey
global url

#----VOREINSTELLUNGEN------------------------------------
# in der "config.json" sind alle Vor-Einstellungen enthalten. 
#
data = f.getData()
apiKey = data['meraki']['apiKey']
url = data['meraki']['url']
netId = data['meraki']['netId'] #'L_706502191543760665' org: mgb test netzwerk: devnetch
payload = {}
#print(data) # print(data['meraki']['apiKey'])
#----VOREINSTELLUNGEN------------------------------------


organisations = f.get('organizations',payload)
print(organisations)

networks = f.get('networks/' + netId,payload)
print(networks)


# VLAN ---------------------------------------
vlansEnabledState = f.get('networks/' + netId + '/vlansEnabledState',payload)
f.printa('vlansEnabledState',vlansEnabledState)
print(vlansEnabledState['enabled'])
print(type(vlansEnabledState['enabled']))

if vlansEnabledState['enabled'] is False:
    # VLANS einschalten
    payload = {"enabled": True}
    vlansEnabledStatePut = f.put('networks/' + netId + '/vlansEnabledState',payload)
    f.printa('vlansEnabledStatePut',vlansEnabledStatePut)

vlans = f.get('networks/' + netId + '/vlans',payload)
f.printa('vlans',vlans)

f.printJson(vlans)


payload = {"id":"10","name":"My VLAN","subnet":"192.168.128.0/24","applianceIp":"192.168.128.2"}
makevlans = f.post('networks/' + netId + '/vlans',payload)
f.printa('makevlans',makevlans)

vlans = f.get('networks/' + netId + '/vlans',payload)
f.printa('vlans',vlans)





# -------------------------SUPPORT-----------------------------
# https://de.python-requests.org/de/latest/user/quickstart.html
# https://dashboard.meraki.com/api_docs/v0#enable/disable-vlans-for-the-given-network
# https://developer.cisco.com/meraki/api/
# 
# 
# 
# 
# 
# -----------------------------------------------------------------


