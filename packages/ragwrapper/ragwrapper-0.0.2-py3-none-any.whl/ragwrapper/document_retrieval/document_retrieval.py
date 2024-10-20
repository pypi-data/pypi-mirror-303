
from exception import MissingResourceError
from utils import get_unique_union


class DocumentRetrieval:
    def __init__(self, retriever, query, query_chain):
        self.retriever = retriever
        self.user_query = query
        self.query_chain = query_chain
        self.retrieval_chain = None
        self.docs = None


class MultiQueryRetrieval(DocumentRetrieval):
    def __init__(self, retriever, query, query_chain):
        super().__init__(retriever=retriever, query=query, query_chain=query_chain)

    def retrieve_documents(self):
        if (self.retriever is not None):
            raise MissingResourceError('retriever')

        if (self.user_query is not None):
            raise MissingResourceError('query')

        if (self.query_chain is not None):
            raise MissingResourceError('query chain')

        self.retrieval_chain = (self.query_chain |
                                self.retriever.map() |
                                get_unique_union)

        self.docs = self.retrieval_chain.invoke({"questions": self.user_query})

        print("Number of Documents : ", len(self.docs))

        return (self.retrieval_chain, self.docs)
