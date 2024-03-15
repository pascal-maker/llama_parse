import os
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
import lancedb
from langchain_community.vectorstores import LanceDB
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import HuggingFaceHub

# Put the token values inside the double quotes
HF_TOKEN = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

# Loading the web url and data (optional)
url_loader = WebBaseLoader("https://libstore.ugent.be/fulltxt/RUG01/003/157/601/RUG01-003157601_2024_0001_AC.pdf")

# Ensure the correct path to your PDF file is provided below (replace with your path)
documents_loader = PyPDFLoader("./Masterproef_ArthurSemay.pdf")  # Load single PDF

# Creating the instances
url_docs = url_loader.load() if url_loader else []  # Load web data if available
data_docs = documents_loader.load()

# Combining all the data that we ingested
docs = url_docs + data_docs

# Splitting documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# Embedding setup
embedding_model_name = 'sentence-transformers/all-MiniLM-L6-v2'
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name, model_kwargs={'device': 'cpu'})

# Embedding query (optional)
query = "Hello I want to see the length of the embeddings for this document."
len(embeddings.embed_documents([query])[0])  # Uncomment to check embedding length

# LanceDB setup
db = lancedb.connect("lance_database")
table = db.create_table(
    "rag_sample",
    data=[
        {
            "vector": embeddings.embed_query("Hello World"),
            "text": "Hello World",
            "id": "1",
        }
    ],
    mode="overwrite",
)

docsearch = LanceDB.from_documents(chunks, embeddings, connection=table)

# Prompt setup
template = """
{query}
"""
prompt = ChatPromptTemplate.from_template(template)

# Retriever setup
retriever = docsearch.as_retriever(search_kwargs={"k": 3})
docs = retriever.get_relevant_documents("Can you give me a summary of \"https://libstore.ugent.be/fulltxt/RUG01/003/157/601/RUG01-003157601_2024_0001_AC.pdf\"?")

# Model setup
llm_repo_id = "huggingfaceh4/zephyr-7b-alpha"
model_kwargs = {"temperature": 0.5, "max_length": 4096, "max_new_tokens": 2048}
model = HuggingFaceHub(repo_id=llm_repo_id, model_kwargs=model_kwargs)

# RAG chain setup
rag_chain = (
    {"context": retriever, "query": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# Invoke RAG chain with a question
response = rag_chain.invoke("Can you give me a summary of \"https://libstore.ugent.be/fulltxt/RUG01/003/157/601/RUG01-003157601_2024_0001_AC.pdf\"?")
print(response)
