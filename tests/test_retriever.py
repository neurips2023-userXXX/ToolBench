from action_generator.components.retriever import (
    RetrieverWithBM25,
    RetrieverWithEmbedding,
)


def test_bm25_retriever():
    retriever = RetrieverWithBM25("data/virtual_home/v0/functions", top_k=10)
    candidate_documents = retriever("Apply lotion on agent face")
    print("".join(candidate_documents))
    print(" ------------------ ")


def test_dense_retriever():
    # No dataset's prepared in this way for now
    return
    retriever = RetrieverWithEmbedding("data/virtualhome/v0/functions", top_k=10)
    candidate_documents = retriever("Apply lotion on agent face")
    print("".join(candidate_documents))
    print(" ------------------ ")
