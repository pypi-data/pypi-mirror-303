'''
2024 Bjoern Annighoefer
'''

from eoq3.value import STR
from eoq3.command import Hel, Get
from eoq3.config import Config
from eoq3.serializer import TextSerializer
from eoq3.util import GenerateSessionId

from ..ecoreconversionoptions import EcoreConversionOptions
from ..saveecorefile import SaveEcoreFile

from eoq3autobahnws.autobahnwsdomainclient import AutobahnWsDomainClient

import argparse

'''
MAIN: Execution starts here
'''            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reads one or more eoq3 files and executes the files it to ')
    parser.add_argument('--outfile', metavar='outfile', type=str, default='model.eoq', help='the file to be downloaded', dest='outfile')
    parser.add_argument('--rootobj', metavar='rootobj', type=str, default='(/*MDB)', help='A query retrieving the model elemen to be downloaded.', dest='rootobj')
    #user model settings
    parser.add_argument('--metafile', metavar='metafile', type=str, default=None, help='the .ecore file (only necessary if a user model is loaded. Otherwise infile will be the metafile.)', dest='metafile')
    parser.add_argument('--savemetamodel', metavar='savemetamodel', type=int, default=0, help='save also the meta-model (only applicable if a user model is saved.)', dest='savemetamodel')
    #domain settings
    parser.add_argument('--host', metavar='host', type=str, default='localhost', help='host address', dest='host')
    parser.add_argument('--port', metavar='port', type=int, default=5161, help='host TCP port', dest='port')
    parser.add_argument('--user', metavar='user', type=str, default=None, help='If given, use this user to login', dest='user')
    parser.add_argument('--pw', metavar='pw', type=str, default=None, help='Credential to authorize the user', dest='pw')
    #ecore conversion options
    # parser.add_argument('--subpackages', metavar='subpackages', type=int, default=1, help='conversion options: include subpackages (only in case of a *.ecore is converted)', dest='subpackages')
    # parser.add_argument('--enums', metavar='enums', type=int, default=1, help='conversion options: include enums (only in case of a *.ecore is converted)', dest='enums')
    # parser.add_argument('--documentation', metavar='documentation', type=int, default=1, help='conversion options: include documentation (only in case of a *.ecore is converted)', dest='documentation')
    # parser.add_argument('--constraints', metavar='constraints', type=int, default=0, help='conversion options: include constraints (only in case of a *.ecore is converted)', dest='constraints')
    # parser.add_argument('--permissions', metavar='permissions', type=int, default=0, help='conversion options: include permissions (only in case of a *.ecore is converted)', dest='permissions')
    # parser.add_argument('--muteupdate', metavar='muteupdate', type=int, default=0, help='if true, UPD commands are muted', dest='muteupdate')
    # parser.add_argument('--maxstrlen', metavar='maxstrlen', type=int, default=-1, help='limit the length of strings (default=-1=infinit)', dest='maxstrlen')
    # parser.add_argument('--maxstrtrunsym', metavar='maxstrtrunsym', type=str, default='...', help='is added at the end of the string if truncated (default=...)', dest='maxstrtrunsym')
    # parser.add_argument('--translatechars', metavar='translatechars', type=int, default=0, help='if true, certian characters in strings are replaced', dest='translatechars')
    # parser.add_argument('--translatetable', metavar='translatetable', type=str, default=" _:_\n#-%\r_\t_,_/_(_)_[_]_{_}_;_\\_=_", help='a sequence of chars to be replaced. Each two consecutive chars are a pair of search and replacement char.', dest='translatetable')
    # parser.add_argument('--packageidfeat', metavar='packageidfeat', type=str, default='name', help='name or nsURI (default=name)', dest='packageidfeat')
    args = parser.parse_args()
    print("*******************************************")
    print("*           saveecorefilewscli           *")
    print("*******************************************")
    print("outfile:        %s"%(args.outfile))
    print("rootobj:        %s"%(args.rootobj))
    print("metafile:       %s"%(args.metafile))
    print("savemetamodel:  %s"%(args.savemetamodel))
    print("host:           %s"%(args.host))
    print("port:           %d"%(args.port))
    print("user:           %s"%(args.user))
    print("pw:             %s"%("******" if args.pw else None))
    # print("subpackages:    %d"%(args.subpackages))
    # print("enums:          %d"%(args.enums))
    # print("documentation:  %d"%(args.documentation))
    # print("constraints:    %d"%(args.constraints))
    # print("permissions:    %d"%(args.permissions))
    # print("muteupdate:     %d"%(args.muteupdate))
    # print("maxstrlen:      %d"%(args.maxstrlen))
    # print("maxstrtrunsym:  %s"%(args.maxstrtrunsym))
    # print("translatechars: %d"%(args.translatechars))
    # print("packageidfeat:  %s"%(args.packageidfeat))
    print("*******************************************")
    #eoq config    
    config = Config()
    config.remoteCmdSerializer = "TXT"
    config.remoteRawLogging = True
    #config.connectTimeout = 1
    #set conversions options
    options = EcoreConversionOptions()
    # options.includeSubpackes = bool(args.subpackages)
    # options.includeEnums = bool(args.enums)
    # options.includeDocumentation = bool(args.documentation)
    # options.includeConstraints = bool(args.constraints)
    # options.includePermissions = bool(args.permissions)
    # options.muteUpdate = bool(args.muteupdate)
    # options.maxStrLen = args.maxstrlen
    # options.maxStrTruncationSymbol = args.maxstrtrunsym
    # options.translateChars = bool(args.translatechars)
    # if(args.translatechars):
    #     if(len(args.translatetable)%2 != 0 ):
    #         raise ValueError("translatetable must have even length.")
    #     #create tuples from char pairs
    #     options.translateTable = [(args.translatetable[i],args.translatetable[i+1]) for i in range(len(args.translatetable)-1)]
    # options.packageIdFeature = args.packageidfeat
    #interpret commands
    sessionId = None
    #create client
    domain = AutobahnWsDomainClient(args.host,args.port,config=config)
    try:
    #login if desired
        if(args.user and args.pw):
            sessionId = GenerateSessionId()
            domain.Do(Hel(STR(args.user),STR(args.pw)),sessionId)
        #obtain the root obj
        qrySerializer = TextSerializer()
        rootQry = qrySerializer.DesQry(args.rootobj)
        rootObj = domain.Do( Get(rootQry), sessionId)
        SaveEcoreFile(args.outfile,rootObj,domain,sessionId,args.metafile,args.savemetamodel,options)
        print('Download complete.')
    finally:
        #close domain
        domain.Close()
        
    