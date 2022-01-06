from pyravendb.store import document_store

class Query():
    def setUp (self):
        # Configurações de acesso ao RavenDB da guiabdo: "usando PFX file para certificação"
        urls = "https://a.rdbguiando.ravendb.community"
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        self.store =  document_store.DocumentStore(urls=urls, database="automacao-faturas", certificate=cert)
        self.store.initialize()
          
    def query_where (self):
        # Query procurando pelo índice do banco Ex: where(informar no nome da coluna no banco, informar o valor procurado).
        with self.store.open_session() as session:
            query_results = list(session.query().where(id="62f783c8445a39954ec8e00e51fc0559"))
            print(query_results[0].id)
            print(len(query_results))
            print('------------------------------')
            
    def query_where_equals (self):
        # Query procurando um ou outro where basta apagar ".adn_also()". Com isso funciona como "and".
        with self.store.open_session() as session:
            query_results = list(session.query().where_equals("dt_vencimento", "01/09/2021").and_also().where_equals("vl_total", "314,22"))
            print(query_results[0].vl_total)
            print(query_results[0].dt_vencimento)
            print(len(query_results))
            print('------------------------------')
            
    def query_on_date_time_range(self):
        # Query procurando por range da datas.
        with self.store.open_session() as session:
           query_results = list(session.query(collection_name="Parseamentos").where_between("at", '01/09/2021', '31/09/2021'))
           print(query_results)
           print(len(query_results))
           print('------------------------------')
            
            

Query_start = Query()
Query_start.setUp()
Query_start.query_where()
Query_start.query_where_equals()
Query_start.query_on_date_time_range()
