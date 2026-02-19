def build_grounded_prompt(query: str, retrieved_docs):
    context_blocks = []

    for doc in retrieved_docs:
        section = doc.metadata.get("section_title", "")
        subsection = doc.metadata.get("subsection_title", "")
        content = doc.page_content

        block = f"[{section} | {subsection}]\n{content}"
        context_blocks.append(block)

    context_text = "\n\n".join(context_blocks)

    prompt = f"""
You are a technical assistant answering questions strictly using the provided context.

If the answer is not present in the context, respond with:
"The answer is not available in the provided document."

Context:
{context_text}

Question:
{query}

Instructions:
- Answer only using the context above.
- Cite section titles in parentheses.
- Do not use outside knowledge.
"""

    return prompt
