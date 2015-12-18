import ConfigParser as cp

config = cp.RawConfigParser()
config.read('config.cfg')

host=config.get("connections","host")
port=config.getint("connections","port")
state=config.get("connections","state")
server=config.get("connections","server")

clientname=config.get("client","name")
