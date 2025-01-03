from denser_retriever.embeddings import SentenceTransformerEmbeddings
from denser_retriever.keyword import (
    ElasticKeywordSearch,
    create_elasticsearch_client,
)
from denser_retriever.reranker import HFReranker
from denser_retriever.vectordb.milvus import MilvusDenserVectorDB

index_name = "unit_test_retriever"

milvus = MilvusDenserVectorDB(
    top_k=5,
    connection_args={"uri": "http://localhost:19530"},
    auto_id=True,
    drop_old=True
)

elasticsearch = ElasticKeywordSearch(
    top_k=5,
    es_connection=create_elasticsearch_client(url="http://localhost:9200"),
    drop_old=True
)
reranker = HFReranker(model_name="cross-encoder/ms-marco-MiniLM-L-6-v2", top_k=5)

embeddings = SentenceTransformerEmbeddings(
    "sentence-transformers/all-MiniLM-L6-v2", 384, True
)