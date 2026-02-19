from langchain_core.documents import Document
from src.chunking.chunker import chunk_text_by_tokens
from src.config import CHUNK_SIZE, CHUNK_OVERLAP, SOURCE_NAME


def classify_chunk_type(section_title: str, subsection_title: str) -> str:
    title = subsection_title.lower()

    if any(word in title for word in ["motivation", "overview", "background"]):
        return "concept"

    if any(word in title for word in ["method", "architecture", "training"]):
        return "method"

    if any(word in title for word in ["experiment", "evaluation", "result"]):
        return "result"

    if "evaluation" in section_title.lower():
        return "result"

    return "concept"


def build_documents(section_objects):
    documents = []

    for sec in section_objects:
        section_title = sec["section_title"]

        for sub in sec["subsections"]:
            subsection_title = sub["subsection_title"]
            text = " ".join(sub["content"])

            chunks = chunk_text_by_tokens(text)

            chunk_type = classify_chunk_type(section_title, subsection_title)

            for idx, chunk in enumerate(chunks):
                metadata = {
                    "section_title": section_title,
                    "subsection_title": subsection_title,
                    "chunk_index": idx,
                    "chunk_type": chunk_type,
                    "source": SOURCE_NAME
                }

                documents.append(
                    Document(
                        page_content=chunk,
                        metadata=metadata
                    )
                )

    return documents
