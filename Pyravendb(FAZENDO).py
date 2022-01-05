from pyravendb.store import document_store
from IPython.display import display

store = document_store.DocumentStore("http://live-test.ravendb.net", "DemoUser-0c45ed3e-37e7-48e7-9a7a-e0de6613a197")
#store = document_store.DocumentStore("https://a.rdbguiando.ravendb.community", "automacao-faturas")

store.initialize()

#url guiando << https://a.rdbguiando.ravendb.community >>
#Database    << automacao-faturas >>

#url teste << http://live-test.ravendb.net >>
#Database    << DemoUser-0c45ed3e-37e7-48e7-9a7a-e0de6613a197 >>

with store.open_session() as session:
         query_results = list(session.query().where(Name="Speedy Express"))
         display(query_results)
         print(len(query_results))

with store.open_session() as session:
    query_results = list(session.query().where_starts_with("Name", "S"))
    display(query_results)
    print(len(query_results))

