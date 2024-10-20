from data_ingestion.vectorDB.Loading.data_loading import WebBaseDataLoader
from data_ingestion.vectorDB.chunking.data_splitting import RecursiveSplitter
from data_ingestion.vectorDB.embedding.data_embeddings import HuggingFaceEmbeddings
from data_ingestion.vectorDB.indexing.data_indexing import FAISSIndexing
from dotenv import load_dotenv, find_dotenv

import os
load_dotenv(find_dotenv())


class DataIngestion:
    def __init__(self) -> None:
        self.loader = None
        self.docs = None
        self.textsplitter = None
        self.splits = None
        self.embeddings = None
        self.index = None
        self.vectore_store = None

    def data_loading(self):

        if os.getenv('loader_type') == "web-base":
            self.loader = WebBaseDataLoader(web_paths=os.getenv('web_path'),
                                            content_class=os.getenv('content_class'))
            self.docs = self.loader.loading()

    def data_splitting(self):
        if self.docs is not None:
            self.textsplitter = RecursiveSplitter(self.docs,
                                                  chunk_size=os.getenv('chunk_size'),
                                                  chunk_overlap=os.getenv('chunk_overlap'))
            self.splits = self.textsplitter.text_splitting()

    def data_embedding(self):
        embeddings_model = HuggingFaceEmbeddings()
        self.embeddings = embeddings_model.create_embeddings()

    def data_indexing(self):
        if (self.splits is not None) and (self.embeddings is not None):
            if os.getenv('index_type') == 'faiss':
                self.index = FAISSIndexing(self.splits, self.embeddings,
                                           index_path=os.getenv('index_path'))
                self.vectore_store = self.index.index_embeddings()
                self.index.save_index()

    def ingest(self):
        self.data_loading()
        print("loading done ..")
        self.data_splitting()
        print("splitting done ..")
        self.data_embedding()
        print("embedding done ..")
        self.data_indexing()
        print("indexing done ..")


if __name__ == "__main__":

    data_ingestion_pipeline = DataIngestion()
    data_ingestion_pipeline.ingest()
    print("ingestion completed.")
