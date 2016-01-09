import ConfigParser as cp

config = cp.RawConfigParser()
config.read('config.cfg')

host=config.get("connections","host")
port=config.getint("connections","port")
state=config.get("connections","state")
server=config.get("connections","server")

userName=config.get("client","userName")
homeName=config.get("client","homeName")

