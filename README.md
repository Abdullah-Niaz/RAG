# Retrieval Augmented Generation (RAG):

Retrieval Augmented Generation, commonly called RAG, is an AI architecture that improves the accuracy, reliability, and freshness of answers produced by large language models. In simple language, RAG combines two components.

1. A **retriever** that finds relevant information from an external data source.
2. A **generator** (like GPT) that reads the retrieved information and produces a final answer.

Traditional language models rely only on what they learned during training. They do not know information added to the world after their training cutoff. They can also hallucinate when they do not know something. RAG solves these problems by giving the model access to a real knowledge base at the moment of answering.
