from pyravendb.store import document_store

# urls = "https://a.rdbguiando.ravendb.community/studio/index.html#databases"


# #########################################
# # use PFX file
# cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
# #########################################


# # use PEM file
# # cert = ("/path/to/cert.pem")


# ###########################################
# #path = 'C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate'
# # use cert / key files
# #cert = (f'{path}/victormagalhaes.client.certificate.crt', f'{path}/victormagalhaes.client.certificate.key')
# ###########################################


# store =  document_store.DocumentStore(urls=urls, database="automacao-faturas", certificate=cert)
# store.initialize() 


# with store.open_session() as session:
#     foo = session.load("foos/1")
   
#---------------------------------------------------------------------------------------------------------------------------------

store =  document_store.DocumentStore(urls=["http://localhost:8080"], database="PyRavenDB")
store.initialize()
with store.open_session() as session:
    foo = session.load("foos/1")