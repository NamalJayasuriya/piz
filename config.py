import ConfigParser as cp

config = cp.RawConfigParser()
config.read('config.cfg')

hostName=config.get("switch","switch-uri")
port=config.getint("switch","port")
state=config.get("switch","state")
server=config.get("switch","switch-name")

userName=config.get("device","owner-name")
homeName=config.get("device","device-name")
dstate=config.get("device","state")

gpioPorts=config.items("gpio")
sws={}
for ports in gpioPorts:
    #print ports[0],ports[1]
    sws[ports[0]]=int(ports[1])

#print 'Switch-URL',host
#print 'Port Number',port
#print state
#print 'Switch Name',server
#print 'Owner Name',userName
#print 'Device Name',homeName
#print 'GPIO ports',gpioPorts
#print dstate
