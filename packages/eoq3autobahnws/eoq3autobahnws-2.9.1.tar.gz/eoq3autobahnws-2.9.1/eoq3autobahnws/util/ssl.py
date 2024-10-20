'''
Helper functions for setting up secure websockets

 2022 Bjoern Annighoefer
'''

import ssl


def CreateSelfSignedServerSslContext(certificatePemFile:str, keyPemFile:str, password:str=None)->ssl.SSLContext:
    ''' Returns an SSL context for a wss server using a self created certificate
    DO NOT USE IN PRODUCTION ENVIRONMENTS!
    '''
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certificatePemFile, keyPemFile, password=password)
    return context


def CreateClientSslContextForSelfSignedServerCert(certificatePemFile:str)->ssl.SSLContext:
    ''' Returns an SSL context for a client connecting to a wss server using a self-created certificate. 
    Must give the path to the servers pem file.
    Does not check the host name.
    DO NOT USE IN PRODUCTION ENVIRONMENTS!
    '''
    context = ssl.create_default_context()
    context.check_hostname = False # Connecting by IP
    context.load_verify_locations(certificatePemFile)
    return context
    