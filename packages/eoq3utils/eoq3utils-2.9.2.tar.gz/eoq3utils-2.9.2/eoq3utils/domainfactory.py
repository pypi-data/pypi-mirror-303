'''
 DomainFactory offers help to create different kinds of domains with the same interface
 Bjoern Annighoefer 2024
'''

from eoq3pyecoremdb import PyEcoreMdb

from eoq3.domainwrappers import DomainToProcessWrapper,DomainPool
from eoq3.domain import Domain
from eoq3.domainwithmdb import DomainWithMdb
from eoq3.config import Config,EOQ_DEFAULT_CONFIG
from eoq3.error import EOQ_ERROR_INVALID_VALUE

from typing import Dict, List, Any

class DOMAIN_TYPES:
    LOCAL = 1
    LOCALPROCESS = 2
    MULTITHREAD_DOMAINPOOL = 3
    MULTIPROCESS_DOMAINPOOL = 4
    TCPCLIENT = 5
    WSCLIENT = 6
    
def CreateLocalDomain(config:Config=EOQ_DEFAULT_CONFIG)->Domain:
    '''Creates the simplest type of domain: a local 
    local command processor with MDB
    '''
    mdb = PyEcoreMdb(config=config)
    domain = DomainWithMdb(mdb,config=config)
    return domain
    
def DomainFactory(domainFactoryArgs:dict):
    '''The function that is called in the process to create the domain
    '''
    return CreateLocalDomain()

def ValidateDomainSettings(expectedFields:List[str], domainSettings:Dict[str,Any])->None:
    for f in expectedFields:
        if(f not in domainSettings):
            raise EOQ_ERROR_INVALID_VALUE("domainSettings miss %s"%(f))
        

def CreateDomain(domainType:int, domainSettings:Dict[str,Any], config:Config=EOQ_DEFAULT_CONFIG)->Domain:
    domain = None
    if(DOMAIN_TYPES.LOCAL==domainType):
        domain = CreateLocalDomain(config)
    elif(DOMAIN_TYPES.LOCALPROCESS==domainType):
        domain = DomainToProcessWrapper(DomainFactory)
    elif(DOMAIN_TYPES.MULTITHREAD_DOMAINPOOL==domainType):
        ValidateDomainSettings(["numberOfDomainWorkers"],domainSettings)
        domain = DomainPool([DomainWithMdb(PyEcoreMdb(config=config),config=config) for i in range(domainSettings["numberOfDomainWorkers"])],shallForwardSerializedCmds=False)
    elif(DOMAIN_TYPES.MULTIPROCESS_DOMAINPOOL==domainType):
        ValidateDomainSettings(["numberOfDomainWorkers"],domainSettings)
        domain = DomainPool([DomainToProcessWrapper(DomainFactory,config=config) for i in range(domainSettings["numberOfDomainWorkers"])],shallForwardSerializedCmds=True)
    elif(DOMAIN_TYPES.TCPCLIENT==domainType):
        ValidateDomainSettings(["host","port","startServer"],domainSettings)
        from eoq3tcp.tcpdomainclient import TcpDomainClient
        if(domainSettings["startServer"]): #for testing purpose it can be useful to start a matching host
            from eoq3tcp.tcpdomainhost import TcpDomainHost
            server = {}
            server["innerDomain"] = CreateLocalDomain(config)
            server["host"] = TcpDomainHost(server["innerDomain"],False,domainSettings["host"],domainSettings["port"],config=config)
            try:
                domain = TcpDomainClient(domainSettings["host"],domainSettings["port"],config=config)
                domain._server = server
            except Exception as e:
                # make sure the server is closed if client creating failed
                server["host"].Stop()
                server["innerDomain"].Close()
                raise e
        else:
            domain = TcpDomainClient(domainSettings["host"],domainSettings["port"],config=config)
    elif(DOMAIN_TYPES.WSCLIENT==domainType):
        ValidateDomainSettings(["host","port","startServer"],domainSettings)
        from eoq3autobahnws.autobahnwsdomainclient import AutobahnWsDomainClient
        if(domainSettings["startServer"]): #for testing purpose it can be useful to start a matching host
            from eoq3autobahnws.autobahnwsdomainhost import AutobahnWsDomainHost
            server = {}
            server["innerDomain"] = CreateLocalDomain(config)
            server["host"] = AutobahnWsDomainHost(server["innerDomain"],False,domainSettings["host"],domainSettings["port"],config=config)
            try:
                domain = AutobahnWsDomainClient(domainSettings["host"],domainSettings["port"],config=config)
                domain._server = server
            except Exception as e:
                # make sure the server is closed if client creating failed
                server["host"].Stop()
                server["innerDomain"].Close()
                raise e
        else:
            domain = AutobahnWsDomainClient(domainSettings["host"],domainSettings["port"],config=config)
    else:
        raise ValueError("Kind of domain %s is unknown"%(str(domainType)))
    return domain

def CleanUpDomain(domain)->None:
    domain.Close()
    if(hasattr(domain,"_server")):
        domain._server["host"].Stop()
        domain._server["innerDomain"].Close()
        