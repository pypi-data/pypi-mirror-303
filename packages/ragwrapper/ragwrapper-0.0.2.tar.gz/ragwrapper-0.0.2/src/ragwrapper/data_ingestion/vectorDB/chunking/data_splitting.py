from langchain.text_splitter import RecursiveCharacterTextSplitter


class DataSplitting:
    def __init__(self):
        pass


class RecursiveSplitter(DataSplitting):

    def __init__(self, docs, chunk_size, chunk_overlap):
        super().__init__()
        self.docs = docs
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = None
        self.splits = None

    def text_splitting(self):
        self.text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=int(self.chunk_size),
                                                                                  chunk_overlap=int(self.chunk_overlap))
        self.splits = self.text_splitter.split_documents(self.docs)

        return self.splits
