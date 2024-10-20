from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain_core. output_parsers import StrOutputParser
from LLMOps.response_generation.response_prompts_template import reponse_prompt_template
from exception import MissingResourceError, ResponseGenerationError


class ResponseGeneration:
    def __init__(self, retrieval_chain, llm, query, response_prompt=reponse_prompt_template):
        self.retrieval_chain = retrieval_chain
        self.llm = llm
        self.user_query = query
        self.prompt = ChatPromptTemplate.from_template(response_prompt)
        self.response_chain = None
        self.response = None

    def generate_response(self):

        if (self.retrieval_chain is not None):
            raise MissingResourceError('retriever chain')

        if (self.llm is not None):
            raise MissingResourceError('LLM Model')

        if (self.prompt is not None):
            raise MissingResourceError('Response Prompt Template')

        try:
            self.response_chain = (
                {"context": self.response_chain,
                 "question": RunnablePassthrough()}
                | self.prompt
                | self.llm
                | StrOutputParser()
            )

            self.response = self.response_chain.invoke(self.user_query)
            return self.response
        except Exception as e:
            raise ResponseGenerationError(f"ErrorMessage : Response Generation failed due to follwoing exception- {e}")
