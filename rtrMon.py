# rtrMon crawls through routers to fetch monitoring information.
# sys.argv[1] = project
# sys.argv[2] = host
# sys.argv[3] = router

import urllib.request as request
import json
import sys
import os
import subprocess


project = sys.argv[1]
host = sys.argv[2]
router = sys.argv[3]
username = ''
password = ''
adminpwd = ''
rtrResponce = ''
posix = True
pingResponce = ''
traceRouteResponce = ''

# test what OS this is run on.
if os.name == 'nt':
    unix = False


# perform a ping test
def ping(host):
    if posix:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True)
    else:
        output = subprocess.run(['ping', '-n', '20', host], capture_output=True)
    return str(output)[str(output).find('---'):str(output).find('stderr') - 3]


# perform a traceroute
def traceRoute(host):
    if posix:
        output = subprocess.run(['traceroute', host], capture_output=True)
    else:
        output = subprocess.run(['tracert', host], capture_output=True)
    return str(output)[str(output).find('stdout') + 9:str(output).find('stderr') - 3]


# # pull login info from json file.
# with open('./login_info.json') as loginInfo:
#     data = json.load(loginInfo)
#     username = data[project]["username"]
#     password = data[project]["password"]
#     if "adminpwd" in data[project]:
#         adminpwd = data[project]["adminpwd"]

# passman = request.HTTPPasswordMgrWithDefaultRealm()
# passman.add_password(None, host, username, password)
# authhandler = request.HTTPBasicAuthHandler(passman)
# opener = request.build_opener(authhandler)

# # url will differ between routers and may need more then one to pull all the information
# # needed so where and what will be stored in a seperate json file containing a list of
# # routers which can be modified if you need more/less information gathered.
# with open('./routers.json') as routers:
#     data = json.load(routers)
#     routerInfo = data[router]
#     for info in routerInfo:
#         responce = opener.open("http://" + host + info[0])
#         rtrResponce = responce.read()  # testing reply
#         responce.close()


# for line in ping(host).split('\\n'):
#     print(line)
for line in traceRoute(host).split('\\n'):
    print(line)
