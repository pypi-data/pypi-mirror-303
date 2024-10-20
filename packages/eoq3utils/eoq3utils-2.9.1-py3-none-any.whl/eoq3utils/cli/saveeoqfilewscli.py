'''
Takes one or more files with eoq content and uploads it to a websocket domain.
2024 Bjoern Annighoefer
'''

from eoq3.value import STR
from eoq3.command import Get, Hel
from eoq3.config import Config
from eoq3.serializer import TextSerializer
from eoq3.util.eoqfile import SaveEoqFile
from eoq3.util import GenerateSessionId

from eoq3autobahnws.autobahnwsdomainclient import AutobahnWsDomainClient

import argparse

'''
MAIN: Execution starts here
'''            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reads an Mdb, M1 or M2 model and stores to an eoq file')
    parser.add_argument('--outfile', metavar='outfile', type=str, default='model.ecore', help='the file to be downloaded', dest='outfile')
    parser.add_argument('--rootobj', metavar='rootobj', type=str, default='(/*MDB)', help='A query retrieving the model elemen to be downloaded.', dest='rootobj')
    parser.add_argument('--host', metavar='host', type=str, default='localhost', help='host address', dest='host')
    parser.add_argument('--port', metavar='port', type=int, default=5161, help='host TCP port', dest='port')
    parser.add_argument('--checksyntax', metavar='checksyntax', type=int, default=1, help='Whether the syntax shall be checked before execution', dest='checksyntax')
    parser.add_argument('--skipupload', metavar='skipupload', type=int, default=0, help='Do not open the TCP connection, e.g. syntax check only.', dest='skipupload')
    parser.add_argument('--user', metavar='user', type=str, default=None, help='If given, use this user to login', dest='user')
    parser.add_argument('--pw', metavar='pw', type=str, default=None, help='Credential to authorize the user', dest='pw')
    args = parser.parse_args()
    
    print("*******************************************")
    print("*           saveeoqfilewscli              *")
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
    domain = AutobahnWsDomainClient(args.host,args.port,config=config)
    #login if desired
    try:
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
        
    