from src.parsing.section_parser import section_objects
from src.ingestion.build_documents import build_documents

docs = build_documents(section_objects)

print(f"Total documents created: {len(docs)}\n")

for d in docs[:3]:
    print(d.metadata)
    print(d.page_content[:200])
    print("-" * 50)
