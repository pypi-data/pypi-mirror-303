# eoq3utils - Swiss Army knife package for EOQ3

Contains API, CLI and service utils that ease the working with EOQ3. 

Furthermore, installing this will all EOQ3 packages at once, i.e. 

* eoq3
* eoq3conceptsgen
* eoq3pyaccesscontroller
* eoq3pyactions
* eoq3pyecoreutils 
* eoq3pyecoremdb
* eoq3pyecorempl
* eoq3autobahnws
* eoq3tcp

## Usage

### API

#### Domain Factory

To create and close different kind of domains easily, CreateDomain and CleanUpDOmain can be used. 
The example shows how to create and clean up different types of domains with the same commands.
Parameters are individual.

    from eoq3utils import DOMAIN_TYPES, CreateDomain, CleanUpDomain
	
	PARAMS = []
	PARAMS.append( ParameterSet(n,{"kindOfDomain" : DOMAIN_TYPES.LOCAL                  ,"domainSettings": {}})); #PyecoreMdb
	PARAMS.append( ParameterSet(n,{"kindOfDomain" : DOMAIN_TYPES.LOCALPROCESS           ,"domainSettings": {}})); #DomainToProcessWrapper 
	PARAMS.append( ParameterSet(n,{"kindOfDomain" : DOMAIN_TYPES.MULTITHREAD_DOMAINPOOL ,"domainSettings": {"numberOfDomainWorkers" : 2}})); #DomainPool
	PARAMS.append( ParameterSet(n,{"kindOfDomain" : DOMAIN_TYPES.MULTIPROCESS_DOMAINPOOL,"domainSettings": {"numberOfDomainWorkers" : 2}})); #DomainPool in process
	PARAMS.append( ParameterSet(n,{"kindOfDomain" : DOMAIN_TYPES.TCPCLIENT              ,"domainSettings": {"host": "127.0.0.1", "port": 6141, "startServer": False }})); # TCP client only
	PARAMS.append( ParameterSet(n,{"kindOfDomain" : DOMAIN_TYPES.WSCLIENT               ,"domainSettings": {"host": "127.0.0.1", "port": 5141, "startServer": True }})); # WS client and host (server is also cleaned up automatically with CleanUpDomain)
	
	for p in PARAMS:
	    domain = CreateDomain(p.kindOfDomain, p.domainSettings)
	    #TODO: do something with the domain
	    CleanUpDomain(resource.domain)


### CLI

#### eoq3utils.cli.loadeoqfiletcpcli

Upload an eoq file to a TCP host:

    python -m python -m eoq3utils.cli.loadeoqfiletcpcli --infile "m2model.eoq" --host "127.0.0.1" --port 6141

    python -m python -m eoq3utils.cli.loadeoqfiletcpcli --infile "m1model.eoq" --host "127.0.0.1" --port 6141


#### eoq3utils.cli.loadeoqfilewscli

Upload eoq files to a Web Socket host:

    python -m python -m eoq3utils.cli.loadeoqfilewscli --infile "m2model.eoq" --host "127.0.0.1" --port 5141
     
    python -m python -m eoq3utils.cli.loadeoqfilewscli --infile "m1model.eoq" --host "127.0.0.1" --port 5141


#### eoq3utils.cli.saveeoqfiletcpcli

Download M2 model as eoq file from TCP host:

    python -m eoq3utils.cli.saveeoqfiletcpcli --outfile "m2model.ecore" --rootobj "(/*MDB/*M2MODELS:0)"  --host "127.0.0.1" --port 6141
	
The same for M1 model:

	python -m eoq3utils.cli.saveeoqfiletcpcli --outfile "m1model.ecore" --rootobj "(/*MDB/*M1MODELS:0)"  --host "127.0.0.1" --port 6141


#### eoq3utils.cli.saveeoqfilewscli

Download M2 model as eoq file from Web Socket host:

    python -m eoq3utils.cli.saveeoqfilewscli --outfile "m2model.eoq" --rootobj "(/*MDB/*M2MODELS:0)" -savemetamodel 1 --host "127.0.0.1"  --port 5141
	
The same for M1 model:

	python -m eoq3utils.cli.saveeoqfilewscli --outfile "m1model.ecore" --rootobj "(/*MDB/*M1MODELS:0)"  --host "127.0.0.1" --port 6141


### Service

TODO: make py ws server available here
  
## Documentation

For more information see EOQ3 documentation: https://eoq.gitlab.io/doc/eoq3/

## Author

2024 Bjoern Annighoefer