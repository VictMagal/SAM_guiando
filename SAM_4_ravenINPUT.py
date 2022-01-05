from pyravendb.store import document_store
from IPython.display import display

class Query():
    def setUp (self):
        urls = "https://a.rdbguiando.ravendb.community"
        # use PFX file
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        self.store =  document_store.DocumentStore(urls=urls, database="automacao-faturas", certificate=cert)
        self.store.initialize()
          
    def query_search (self):
        with self.store.open_session() as session:
            query_results = list(session.query().where(file_name="226542-8_20210901.pdf"))
            display(query_results)
            print(len(query_results))

Query_start = Query()
Query_start.setUp()
Query_start.query_search()
