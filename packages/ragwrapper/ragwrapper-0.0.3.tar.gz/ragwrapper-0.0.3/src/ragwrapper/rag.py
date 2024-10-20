from langchain_groq import ChatGroq
from .query_transformation.query_transformation import MultiQueryTransformationPrompt
from .document_retrieval.document_retrieval import MultiQueryRetrieval
from .response_generation.response_generation import ResponseGeneration
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

model = os.getenv("model", "llama3-8b-8192")
llm = ChatGroq(model=model, temperature=0,)  # type: ignore
query = input()
query_transformation_type = "Multi-Query"


class RetrievalAugmentedGeneration:

    def __init__(self, llm, query, retriever):
        self.llm = llm
        self.user_query = query
        self.retriever = retriever
        self.query_chain = None
        self.queries = None

        self.retrieval_chain = None
        self.docs = None

        self.reponse = None

    def query_transformation(self):
        if query_transformation_type == "Multi-Query":
            transformation_instance = MultiQueryTransformationPrompt(self.llm, self.user_query)
            self.query_chain, self.queries = transformation_instance.generate_queries()

    def document_retrieval(self):
        if self.query_chain is not None:
            retrieval_instance = MultiQueryRetrieval(self.retriever, self.query, self.query_chain)
            self.retrieval_chain, self.docs = retrieval_instance.retrieve_documents()

    def response_generation(self):
        response_instance = ResponseGeneration(self.retrieval_chain, self.llm, self.user_query)
        self.reponse = response_instance.generate_response()
