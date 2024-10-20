'''
Takes one or more files with eoq content and uploads it to a TCP domain.
2024 Bjoern Annighoefer
'''

from eoq3.value import STR
from eoq3.command import Hel
from eoq3.config import Config
from eoq3.util.eoqfile import LoadEoqFile, ValidateEoqFile
from eoq3.util import GenerateSessionId

from eoq3tcp.tcpdomainclient import TcpDomainClient

import argparse
from typing import Any

'''
MAIN: Execution starts here
'''            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reads one or more eoq3 files and executes the files it to ')
    parser.add_argument('--infile', metavar='infile', type=str, default='model.eoq', help='the file to be uploaded', dest='infile')
    parser.add_argument('--infile2', metavar='infile2', type=str, default=None, help='(optionally) a second file to be interpreted', dest='infile2')
    parser.add_argument('--infile3', metavar='infile3', type=str, default=None, help='(optionally) a third file to be interpreted', dest='infile3')
    parser.add_argument('--infile4', metavar='infile4', type=str, default=None, help='(optionally) a fourth file to be interpreted', dest='infile4')
    parser.add_argument('--host', metavar='host', type=str, default='localhost', help='host address', dest='host')
    parser.add_argument('--port', metavar='port', type=int, default=5161, help='host TCP port', dest='port')
    parser.add_argument('--checksyntax', metavar='checksyntax', type=int, default=1, help='Whether the syntax shall be checked before execution', dest='checksyntax')
    parser.add_argument('--skipupload', metavar='skipupload', type=int, default=0, help='Do not open the TCP connection, e.g. syntax check only.', dest='skipupload')
    parser.add_argument('--user', metavar='user', type=str, default=None, help='If given, use this user to login', dest='user')
    parser.add_argument('--pw', metavar='pw', type=str, default=None, help='Credential to authorize the user', dest='pw')
    args = parser.parse_args()
    
    infiles = [i for i in [args.infile,args.infile2,args.infile3,args.infile4] if None != i]
    
    print("*******************************************")
    print("*           loadeoqfiletcpcli             *")
    print("*******************************************")
    print("infiles:       %s"%(infiles))
    print("host:          %s"%(args.host))
    print("port:          %d"%(args.port))
    print("checksyntax:   %d"%(args.checksyntax))
    print("skipupload:    %d"%(args.skipupload))
    print("user:          %s"%(args.user))
    print("pw:            %s"%("******" if args.pw else None))
    print("*******************************************")
     
    config = Config()
    config.remoteCmdSerializer = "TXT"
    config.remoteRawLogging = True
    #config.connectTimeout = 1
    
    #first check syntax of all files
    if(args.checksyntax):
        for infile in infiles:
            ValidateEoqFile(infile)
        print('Syntax check complete.')

    #interpret commands
    if(not args.skipupload):
        sessionId = None
        #create client
        domain = TcpDomainClient(args.host,args.port,2**20,b'\x00',config)
        try:
        #login if desired
            if(args.user and args.pw):
                sessionId = GenerateSessionId()
                domain.Do(Hel(STR(args.user),STR(args.pw)),sessionId)
            for infile in infiles:
                LoadEoqFile(infile,domain,sessionId,validateBeforeLoad=False)
            print('Upload complete.')
        finally:
            #close domain
            domain.Close()
        
    