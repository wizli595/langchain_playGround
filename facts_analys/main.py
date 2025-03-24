from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import json

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("facts.txt")
docs = loader.load_and_split(text_splitter)

db = Chroma.from_documents(docs, embeddings, persist_directory="emb")

results = db.similarity_search_with_score("What is an interesting fact about the english language?", k=1)

for result in results:
    print("\n")
    print(result[1])
    print(result[0].page_content)
