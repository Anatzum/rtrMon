# rtrMon crawls through routers to fetch monitoring information.
# sys.argv[1] = project
# sys.argv[2] = host
# sys.argv[3] = router

# import urllib.request as request
# import json
import sys
import os
import asyncio


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
async def ping(host):
    pingProc = await asyncio.create_subprocess_shell('ping -c 20 ' + host,
                                                     stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await pingProc.communicate()
    if stdout:
        output = stdout.decode()
        print(output[:output.find('data.') + 5])
        print(output[output.find('---'):])


# perform a traceroute
async def traceRoute(host):
    if posix:
        traceProc = await asyncio.create_subprocess_shell('traceroute ' + host,
                                                          stdout=asyncio.subprocess.PIPE,
                                                          stderr=asyncio.subprocess.PIPE)
    else:
        traceProc = await asyncio.create_subprocess_shell('tracert ' + host,
                                                          stdout=asyncio.subprocess.PIPE,
                                                          stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await traceProc.communicate()
    if stdout:
        print(stdout.decode())


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


async def main():
    await asyncio.gather(
        ping(host),
        traceRoute(host)
    )

asyncio.run(main())
