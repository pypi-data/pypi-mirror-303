# eoq3autobahnws - Websocket domain client and host using autobahn

A domain server makes a local domain accessible via a WS port.

A domain host connects to a remote domain using WS. 

client and server are based on autobahn: https://autobahn.readthedocs.io/en/latest/index.html
		
## Usage

Define serialization and timeouts

    config = Config()
    config.remoteCmdSerializer = "TXT" #or JSO
    config.connectTimeout = 40

### Host

Imports: 

    from eoq3autobahnws.autobahnwsdomainhost import AutobahnWsDomainHost
	
Create an SSL factory (optional):
	
	def ServerSslFactory(sslFactoryArgs:dict):
        return CreateSelfSignedServerSslContext("ssl/certificate.pem", "ssl/key.pem", "ILS-admin")
	 
Creating a TCP host domain that provides acces to another domain "localDomain", e.g. DomainWithMdb:

    server = AutobahnWsDomainHost(localDomain, True, '127.0.0.1', 5141, nWorkers=N_THREADS, config=config) #no ssh

	server = AutobahnWsDomainHost(localDomain, True, '127.0.0.1', 5141, sslContextFactory=ServerSslFactory, nWorkers=N_THREADS, config=config) #with ssh

### Client

Imports: 

    from eoq3autobahnws.autobahnwsdomainclient import AutobahnWsDomainClient
    from eoq3autobahnws.util import CreateClientSslContextForSelfSignedServerCert
	
Create an SSL factory (optional):

    def ClientSslFactory(domainFactoryArgs:dict): 
        return CreateClientSslContextForSelfSignedServerCert("ssl/certificate.pem")
	 
Connecting to a remote domain:

    domain = AutobahnWsDomainClient('127.0.0.1',5141) #no ssl

	domain = AutobahnWsDomainClient('127.0.0.1',5141,sslContextFactory=ClientSslFactory) #with ssl
	
### Examples

See

* pyeoq/Examples/Eoq3/BasicWebsocketServer.py and
* pyeoq/Examples/Eoq3/BasicWebsocketDomain.py
	

## Documentation

For more information see EOQ3 documentation: https://eoq.gitlab.io/doc/eoq3/

## Author

2024 Bjoern Annighoefer