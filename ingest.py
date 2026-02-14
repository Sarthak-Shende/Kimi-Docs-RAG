from src.parsing.section_parser import section_objects
from src.ingestion.build_documents import build_documents
from src.ingestion.build_index import build_chroma_index


def main():
    print("Building documents...")
    documents = build_documents(section_objects)
    print(f"Total documents: {len(documents)}")

    print("Building Chroma index...")
    build_chroma_index(documents)

    print("Ingestion complete.")


if __name__ == "__main__":
    main()
