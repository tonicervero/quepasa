#!/usr/bin/python

#Quepasa is free software
#Quepasa is meant to perform quick analysis of server problems
#Use quepasa carefully ! this is not a silver bullet or a fix-everything magic script.
#I deliver quepasa with NO WARRANTY
#cervero.tony@gmail.com


# example of usage:
# quepasa -s server -r runbook [-o options] [-g gateway]

import fabric
from fabric.api import *
import argparse
import sys
import os
from inspect import *
import func
from func.func_network import *

def GetFunctions():
    functions = []
    functions_list = [o for o in getmembers(func.func_network) if isfunction(o[1])]
    for function in functions_list:
        functions.append(function[0])
    return functions

def SetFabEnv(opts):
    env.user = opts.serveruser
    env.host = opts.server
    env.hosts.append(opts.server)
    env.host_string = opts.server
    env.port = opts.port
    env.gateway = opts.gateway
    return env

if __name__ == '__main__':

    #Parsing arguments
    parser = argparse.ArgumentParser(description='Quepasa 0.1 diagnosis and troubleshooting tool')
    parser.add_argument('-s','--server', dest='server', help='Target server for runbook', default='127.0.0.1', required=False)
    parser.add_argument('-p','--port', dest='port', help='SSH port for target', default=22, required=False)
    parser.add_argument('-u','--serveruser', dest='serveruser', help='SSH user for target', required=False)
    parser.add_argument('-g','--gateway', dest='gateway', help='Gateway or bastion server to reach the target server', required=False)
    parser.add_argument('-q','--gatewayport', dest='gatewayport', help='Gateway or bastion server ssh port', default=22, required=False)
    parser.add_argument('-r','--runbook', dest='runbook', help='Specific runbook, set of functions for run', required=False)
    parser.add_argument('-f','--function', dest='function', help='Specific function to run', required=False)
    parser.add_argument('-fl', '--function-list', dest='functionlist', help='List the functions available', action='store_false', default='all')
    #   parser.add_argument('-h','--help', dest='help', help='Prints help', required=False)
    opts = parser.parse_args()

    #Format arguments
    #http://docs.fabfile.org/en/1.13/usage/fab.html
    #{'disable_known_hosts': False, 'effective_roles': [], 'tasks': [], 'linewise': False, 'show': ('NO', 'DEFAULT'), 'password': None, 'key_filename': None, 'abort_on_prompts': False, 'skip_unknown_tasks': False,
    # 'reject_unknown_hosts': False, 'skip_bad_hosts': False, 'use_ssh_config': False, 'roledefs': {}, 'gateway': None, 'gss_auth': None,
    # 'keepalive': 0, 'eagerly_disconnect': False, 'rcfile': '.fabricrc', 'path_behavior': 'append', 'hide': ('NO', 'DEFAULT'),
    # 'sudo_prefix': "sudo -S -p '%(sudo_prompt)s' ", 'lcwd': '', 'no_agent': False, 'forward_agent': False, 'remote_interrupt': None,
    # 'port': '22', 'shell': '/bin/bash -l -c', 'version': '1.13.1', 'use_exceptions_for': {'network': False}, 'connection_attempts': 1,
    # 'hosts': ['localhost:8001'], 'gss_deleg': None, 'cwd': '', 'abort_exception': None, 'real_fabfile': None,
    # 'passwords': {}, 'sudo_password': None, 'host_string': None, 'shell_env': {}, 'always_use_pty': True, 'colorize_errors': False,
    # 'exclude_hosts': [], 'all_hosts': [], 'sudo_prompt': 'sudo password:', 'again_prompt': 'Sorry, try again.', 'echo_stdin': True,
    # 'user': 'tony', 'gss_kex': None, 'command_timeout': None, 'path': '',
    #'local_user': 'antonio', 'combine_stderr': True, 'command_prefixes': [], 'dedupe_hosts': True, 'warn_only': False, 'no_keys': False,
    # 'sudo_passwords': {}, 'roles': [], 'fabfile': 'fabfile', 'use_shell': True, 'host': None, 'pool_size': 0, 'system_known_hosts': None, 'prompts': {},
    # 'output_prefix': True, 'command': None, 'timeout': 10, 'default_port': '22', 'ssh_config_path': '.ssh/config',
    # 'parallel': False, 'sudo_user': None, 'ok_ret_codes': [0]}

    env = SetFabEnv(opts)
    #print dir(func.func_network)
    funcList = GetFunctions()

    if not opts.functionlist:
        print 'below the list of functions available:'
        for f in funcList:
            print f
    else:
        function_name = opts.function  # set by the command line options
        if function_name in funcList:
            funcIndex = funcList.index(function_name)
            globals()[funcList[funcIndex]](env)
        else:
            print "Method %s not implemented" % function_name


# before end of execution need to make sure all connections are closed:
    #for key in connections.keys():
    #    connections[key].close()
    #del connections[key]