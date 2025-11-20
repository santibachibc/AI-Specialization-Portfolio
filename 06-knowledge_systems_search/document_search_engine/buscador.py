from whoosh.index import open_dir
from whoosh.qparser import QueryParser

ix = open_dir("indexdir")
qp = QueryParser("content", schema=ix.schema)

while True:
    q = input("\n🔎 Escribe tu consulta (o 'salir'): ")
    if q.lower() in ['salir', 'exit', 'q']:
        break

    query = qp.parse(q)

    with ix.searcher() as searcher:
        results = searcher.search(query, limit=10)
        if results:
            print(f"\n📄 Documentos encontrados ({len(results)}):")
            for r in results:
                print(f" - {r['title']}")
        else:
            print("❌ No se encontraron resultados.")
