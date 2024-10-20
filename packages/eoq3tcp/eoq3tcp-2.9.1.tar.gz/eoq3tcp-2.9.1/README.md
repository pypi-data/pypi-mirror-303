# eoq3tcp - TCP domain client and host

A domain server makes a local domain accessible via TCP port.

A domain host connects to a remote domain using TCP. 
		
## Usage

Define serialization and timeouts

    config = Config()
    config.remoteCmdSerializer = "TXT" #or JSO
    config.connectTimeout = 40

### Host

Imports: 

    from eoq3tcp.tcpdomainhost import TcpDomainHost
	 
Creating a TCP host domain that provides acces to another domain "localDomain", e.g. DomainWithMdb:

	server = TcpDomainHost(localDomain,False,HOST,PORT,2**20,b'\x00',config)

### Client

Imports: 

    from eoq3tcp.tcpdomainclient import TcpDomainClient
	 
Connecting to a remote domain:

	domain = TcpDomainClient(HOST,PORT,2**20,b'\x00',config)
	
### Examples

See

* pyeoq/Examples/Eoq3/BasicTcpServer.py and
* pyeoq/Examples/Eoq3/BasicTcpDomain.py.

## Documentation

For more information see EOQ3 documentation: https://eoq.gitlab.io/doc/eoq3/

## Author

2024 Bjoern Annighoefer

