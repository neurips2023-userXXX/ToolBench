import os
from haystack.document_stores import InMemoryDocumentStore, FAISSDocumentStore
from haystack.nodes import BM25Retriever, EmbeddingRetriever


class RetrieverBase:
    def __init__(self, api_doc_dir, top_k=10):
        self.retriever = None
        self.top_k = top_k

    def __call__(self, query):
        candidate_documents = self.retriever.retrieve(
            query=query,
            top_k=self.top_k,
        )
        return [d.content for d in candidate_documents]

    def get_all_docs(self, api_doc_dir):
        docs = []
        for filename in os.listdir(f"{api_doc_dir}"):
            if filename.startswith("document_store") or filename.startswith(
                "faiss_document_store.db"
            ):
                continue
            with open(f"{api_doc_dir}/{filename}") as f:
                lines = f.readlines()
                content = "".join(lines)

            docs.append({"content": content, "meta": {"name": filename}})
        return docs

    def load_valid_api(self, valid_api_file):
        valid_api_func = []
        with open(valid_api_file) as f:
            for line in f:
                valid_api_func.append(line.strip())
        print(valid_api_func)
        return valid_api_func


class RetrieverWithBM25(RetrieverBase):
    def __init__(self, api_doc_dir, top_k=10):
        super().__init__(api_doc_dir, top_k)
        document_store = InMemoryDocumentStore(use_bm25=True)
        docs = self.get_all_docs(api_doc_dir)
        document_store.write_documents(docs)
        self.retriever = BM25Retriever(document_store=document_store)


class RetrieverWithEmbedding(RetrieverBase):
    def __init__(self, api_doc_dir, top_k=10):
        super().__init__(api_doc_dir, top_k)

        db_path = f"sqlite:///{api_doc_dir}/faiss_document_store.db"
        faiss_path = f"{api_doc_dir}/document_store"
        if os.path.exists(faiss_path):
            document_store = FAISSDocumentStore.load(index_path=faiss_path)
        else:
            document_store = FAISSDocumentStore(
                sql_url=db_path,
                faiss_index_factory_str="Flat",
                embedding_dim=768,
                return_embedding=True,
            )
            docs = self.get_all_docs(api_doc_dir)
            document_store.write_documents(docs)

        self.retriever = EmbeddingRetriever(
            document_store=document_store,
            embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1",
            model_format="sentence_transformers",
        )
        if not os.path.exists(faiss_path):
            document_store.update_embeddings(
                self.retriever, update_existing_embeddings=False
            )
            document_store.save(index_path=faiss_path)
