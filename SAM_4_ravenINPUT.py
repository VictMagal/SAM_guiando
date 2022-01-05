from pyravendb.store import document_store
from IPython.display import display

urls = "https://a.rdbguiando.ravendb.community"

# #########################################
# # use PFX file
cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
# #########################################

# # use PEM file
# # cert = ("/path/to/cert.pem")

# ###########################################
# #use cert / key files
# path = 'C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate'
# cert = (f'{path}/victormagalhaes.client.certificate.crt', f'{path}/victormagalhaes.client.certificate.key')
# ###########################################


store =  document_store.DocumentStore(urls=urls, database="automacao-faturas", certificate=cert)
store.initialize() 

with store.open_session() as session:
         query_results = list(session.query().where(file_name="226542-8_20210901.pdf"))
         display(query_results)
         print(len(query_results))

# with store.open_session() as session:
#     foo = session.load("foos/1")
   
#---------------------------------------------------------------------------------------------------------------------------------

