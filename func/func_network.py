#functions for network
import socket
import fabric
from fabric.api import *

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

# Simple SSH connection checker
def TestSSH(env):
    print 'Testing SSH connection to ' + env.hosts[0] + ':' + str(env.port) + '...'
    with settings(hide('warnings', 'running', 'stderr'),warn_only=True):
        try:
            output = run('echo "HOST:`hostname`: SSH connection succesful"')
            return True
        except Exception as e:
            print(("something's wrong with %s:%s. Exception is %s" % (env.hosts[0], str(env.port), e)))
            return False

# Simple ICMP checker
def TestPing(env):
    print 'Testing ICMP (ping) to ' + env.hosts[0] + ':' + str(env.port) + '...'
