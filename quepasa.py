#!/bin/python

#Quepasa is free software
#Quepasa is meant to perform quick analysis of server problems
#Use quepasa carefully ! this is not a silver bullet or a fix-everything magic script.
#I deliver quepasa with NO WARRANTY
#cervero.tony@gmail.com


# example of usage:
# quepasa -s server -r runbook [-o options] [-g gateway]

import fabric
import argparse
import sys
import os
import socket
from func.func_network import *

if __name__ == '__main__':

    #Parsing arguments
    parser = argparse.ArgumentParser(description='Quepasa diagnosis and troubleshooting tool')
    parser.add_argument('-s','--server', dest='server', help='Target server for runbook', required=True)
    parser.add_argument('-p','--port', dest='port', help='SSH port for target', required=False)
    parser.add_argument('-g','--gateway', dest='gateway', help='Gateway or bastion server to reach the target server', required=False)
    parser.add_argument('-r','--runbook', dest='runbook', help='Specific runbook, set of functions for run', required=False)
    parser.add_argument('-f','--function', dest='function', help='Specific function to run', required=False)
    opts = parser.parse_args()



    TestTCP(opts.server,22)
    print opts.server

