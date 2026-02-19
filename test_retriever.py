from src.retrieval.retriever import retrieve

query = "Why did they design Agent Swarm?"

results = retrieve(query, k=3)

for r in results:
    print(r.metadata)
    print(r.page_content[:300])
    print("-" * 50)
