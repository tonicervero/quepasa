#functions for network
import socket


# Simple TCP connection checker
def TestTCP(env):
    s = socket.socket()
    try:
        s.connect((env.hosts[0], int(env.port)))
        print 'TCP connection connection succesfull!'
        s.close()
        return True
    except Exception as e:
        print("something's wrong with %s:%s. Exception is %s" % (env.hosts[0], env.port, e))
        s.close()
        return False



def TestSSH(env):
    pass

def TestPing(env):
    pass