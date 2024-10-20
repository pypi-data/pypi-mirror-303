
# RAG Automation Wrapper

## Overview
This project provides a Python wrapper around LangChain to automate Retrieval-Augmented Generation (RAG). The package abstracts the RAG workflow into two modular components: Data Ingestion, Retrieval and Generation. The wrapper is designed for seamless integration with various data sources, retrieval methods, and large language models (LLMs), making it easier to prototype and deploy RAG-based systems.

## Key Features
Data Ingestion: Handle various data formats and load them into a retrievable format.
Retrieval: Efficiently search and retrieve relevant data using a combination of query transformation techniques and vector databases.
Generation: Use state-of-the-art LLMs to generate contextually relevant responses based on the retrieved information.
Components

1. Data Ingestion
The ingestion component ingests documents or datasets from various sources, such as plain text, PDFs, CSVs, or databases, and converts them into an indexed format for retrieval. This ensures that your data is well-structured and easily searchable.

Supported data formats:
Text, PDFs, CSVs, JSON
Databases (SQL, NoSQL)

2. Retrieval
The retrieval component is responsible for fetching relevant data from the indexed sources using various search techniques, including vector-based search, keyword-based search, or a hybrid of both.


Support for multiple databases (e.g., FAISS, Elasticsearch)
Query transformation for enhanced search accuracy
Embedding-based retrieval (using sentence-transformers, OpenAI embeddings, etc.)

3. Generation
The generation component utilizes the retrieved data to generate responses using a large language model (LLM). This component can be customized with different models such as OpenAI's GPT, Hugging Face Transformers, or any local LLMs.


LLM-based contextual generation
Support for different temperature and decoding strategies for controlled output
Integration with OpenAI, Hugging Face, or custom LLMs


