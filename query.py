from src.retrieval.retriever import retrieve
from src.generation.answer import GeminiGenerator


def main():
    query = input("Enter your question: ")

    retrieved_docs = retrieve(query, k=3)

    generator = GeminiGenerator()
    answer = generator.generate_answer(query, retrieved_docs)

    print("\n--- Answer ---\n")
    print(answer)


if __name__ == "__main__":
    main()
