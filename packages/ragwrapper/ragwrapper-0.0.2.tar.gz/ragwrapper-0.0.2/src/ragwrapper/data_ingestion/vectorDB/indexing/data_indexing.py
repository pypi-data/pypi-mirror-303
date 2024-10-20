import os
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

index_path = os.getenv('index_path')


class DataIndexing:
    def __init__(self, splits, embeddings):
        self.splits = splits
        self.embeddings = embeddings
        self.vectorstore = None


class FAISSIndexing(DataIndexing):

    def __init__(self, splits, embeddings, index_path):
        super().__init__(splits, embeddings)
        self.index_path = index_path

    def index_embeddings(self):
        self.vectorstore = FAISS.from_documents(documents=self.splits,
                                                embedding=self.embeddings)
        return self.vectorstore

    def save_index(self):
        self.vectorstore.save_local(self.index_path)
