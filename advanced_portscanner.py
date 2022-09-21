#!/usr/bin/python

from socket import *
import optparse
from threading import *


def portScan(tgtHost, tgtPorts):
        #try to get the IP address from the host name, if it fails, print the unknown host message
        try:
                tgtIP = gethostbyname(tgtHost)
        except:
                print("Unknown host %s " %tgtHost)
       
        #try to get the host name from the address
        try:
                tgtName = gethostbyaddr(tgtIP)
                print("[+] Scan results for: " + tgtName[0])
        except:
                print("[+] Scan results for: " + tgtIP)
        setdefaulttimeout(1)
        for tgtPort in tgtPorts:
                t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
                t.start()

def main():
        parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>')                     #prints on the terminal if the user doesn't know what host/port to enter
        parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
        parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports seperated by comma')
        (options, args) = parser.parse_args()
        tgtHost = options.tgtHost
        tgtPorts = str(options.tgtPort).split(',')
        if(tgtHost == None) | (tgtPorts[0] == None):
                print(parser.usage)
                exit(0)
        portScan(tgtHost, tgtPorts)

if (__name__ = '__main__'):
        main()