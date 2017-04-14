#functions for network
import socket

def TestTCP(server, port):
    s = socket.socket()
    try:
        s.connect((server, port))
    except Exception as e:
        print("something's wrong with %s:%d. Exception is %s" % (server, port, e))
    finally:
        s.close()


