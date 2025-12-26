from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from openai import OpenAI
from langchain_community.vectorstores import FAISS
import os
load_dotenv()
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    split_docs = text_splitter.split_documents(documents)
    return split_docs


def store_in_faiss(split_docs, index_path="faiss_index"):
    faiss_index = FAISS.from_documents(documents=split_docs, embedding=OpenAIEmbeddings())
    faiss_index.save_local(index_path)
    return faiss_index


def Query_FAISS(faiss_index, query, k=5):
    results = faiss_index.similarity_search(query, k=k)
    return results

def final_reponse(Rag_results, query):
   
    openai_api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful chatabase assistant to generate the short summarize 3 liner response if you feel like  the question/query is out of the document context then in reposne tell \"its out of document question\"."},
            {"role": "user", "content": f"Based on the following documents: {Rag_results} and the query: {query}, generate a comprehensive response."}
        ]
    )
    return response.choices[0].message.content 


    

if __name__ == "__main__":
    file_path = r"D:\personal_projects\Rag_Lang_Chain\Artificial.pdf"
    documents = load_pdf(file_path)
    split_docs = split_documents(documents)
    faiss_index = store_in_faiss(split_docs)
    query = "Can you tell me my name?"
    results = Query_FAISS(faiss_index, query)
    final_response = final_reponse(results, query)
    print("Final Response:")
    print(final_response)
