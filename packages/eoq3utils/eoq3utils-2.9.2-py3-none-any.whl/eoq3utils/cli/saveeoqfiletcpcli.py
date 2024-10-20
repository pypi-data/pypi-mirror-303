'''
Downloades content from a TCP domain to a eoq file.
2024 Bjoern Annighoefer
'''

from eoq3.value import STR
from eoq3.command import Get, Hel
from eoq3.config import Config
from eoq3.serializer import TextSerializer
from eoq3.util.eoqfile import SaveEoqFile
from eoq3.util import GenerateSessionId

from eoq3tcp.tcpdomainclient import TcpDomainClient

import argparse
        
'''
MAIN: Execution starts here
'''            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reads an Mdb, M1 or M2 model and stores to an eoq file')
    parser.add_argument('--outfile', metavar='outfile', type=str, default='model.eoq', help='the file to be downloaded', dest='outfile')
    parser.add_argument('--rootobj', metavar='rootobj', type=str, default='(/*MDB)', help='A query retrieving the model elemen to be downloaded.', dest='rootobj')
    parser.add_argument('--host', metavar='host', type=str, default='localhost', help='host address', dest='host')
    parser.add_argument('--port', metavar='port', type=int, default=5161, help='host TCP port', dest='port')
    parser.add_argument('--user', metavar='user', type=str, default=None, help='If given, use this user to login', dest='user')
    parser.add_argument('--pw', metavar='pw', type=str, default=None, help='Credential to authorize the user', dest='pw')
    args = parser.parse_args()
    
    print("*******************************************")
    print("*           saveeoqfiletcpcli             *")
    print("*******************************************")
    print("outfile:       %s"%(args.outfile))
    print("rootobj:       %s"%(args.rootobj))
    print("host:          %s"%(args.host))
    print("port:          %d"%(args.port))
    print("user:          %s"%(args.user))
    print("pw:            %s"%("******" if args.pw else None))
    print("*******************************************")
    
    config = Config()
    config.remoteCmdSerializer = "TXT"
    config.remoteRawLogging = True
    #config.connectTimeout = 1
    
    sessionId = None
    #create client
    domain = TcpDomainClient(args.host,args.port,2**20,b'\x00',config)
    try:
        #login if desired
        if(args.user and args.pw):
            sessionId = GenerateSessionId()
            domain.Do(Hel(STR(args.user),STR(args.pw)),sessionId)
        #obtain the root obj
        qrySerializer = TextSerializer()
        rootQry = qrySerializer.DesQry(args.rootobj)
        rootObj = domain.Do( Get(rootQry), sessionId)
        SaveEoqFile(args.outfile,rootObj,domain,sessionId)
        print('Download complete.')
    finally:
        #close domain
        domain.Close()
        
    