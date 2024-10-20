from langchain_community.embeddings import HuggingFaceBgeEmbeddings
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class DataEmbeddings:
    def __init__(self, model):
        self.model = model


class HuggingFaceEmbeddings(DataEmbeddings):
    def __init__(self):
        super().__init__(model=os.getenv('embedding_model'))
        self.model_kwargs = {"device": "cpu"}
        self.encode_kwargs = {"normalize_embeddings": True}
        self.embeddings = None

    def create_embeddings(self):
        self.embeddings = HuggingFaceBgeEmbeddings(
            model_name=self.model,
            model_kwargs=self.model_kwargs,
            encode_kwargs=self.encode_kwargs)
        return self.embeddings
