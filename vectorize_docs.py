from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Create Embedding Instance
embedding = HuggingFaceEmbeddings()

# Create Loader and specify the type of files to load
loader = DirectoryLoader(data="data", 
                         glob="*.pdf",
                         loader_class=UnstructuredFileLoader
                         ) 

documents = loader.load()

# Splits the documents into smaller parts
text_splitter = CharacterTextSplitter(
    chunck_size=2000,
    chunck_overlap=500
)

splitted_docs = text_splitter.split_documents(documents)

# Create the Vector DB
vectordb = Chroma.from_documents(
    documents=splitted_docs,
    embeddings=embedding,
    persist_directories="vector_db_dir"
)

# Done
print("Documents Vectorized")