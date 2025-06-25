import os
from git import Repo
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

file_types = ["*.py", "*.html", "*.css", "*.js", "*.java", "*.sql", "*.json"]

def clone_repo(url, folder="repo_files"):
    if not os.path.exists(folder):
        print("Cloning repository...")
        Repo.clone_from(url, folder)
    else:
        print("Repo already cloned.")
    return folder

def load_files(folder):
    documents = []
    for file_type in file_types:
        loader = DirectoryLoader(folder, glob=f"**/{file_type}", loader_cls=TextLoader)
        documents.extend(loader.load())
    return documents

def get_retriever(documents):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(documents, embeddings)
    return db.as_retriever()

def create_qa_bot(retriever):
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    qa = RetrievalQA.from_chain_type(llm=model, retriever=retriever)
    return qa

if __name__ == "__main__":
    github_url = input("Enter GitHub Repo URL: ")
    
    repo_folder = clone_repo(github_url)
    docs = load_files(repo_folder)
    retriever = get_retriever(docs)
    qa_bot = create_qa_bot(retriever)

    print("\nAsk anything about the repository! (type 'exit' to quit)\n")

    while True:
        question = input("You: ")
        if question.lower() == "exit":
            break
        answer = qa_bot.invoke(question)
        print("\nAnswer:", answer['result'], "\n")
