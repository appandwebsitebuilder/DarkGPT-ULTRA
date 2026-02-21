import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

class InnovationMesh:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.persist_dir = "./data/mesh_db"
        self.vector_db = Chroma(persist_directory=self.persist_dir, embedding_function=self.embeddings)

    def add_idea(self, title: str, description: str, author: str):
        full_text = f"Title: {title} | Description: {description}"
        self.vector_db.add_texts(
            texts=[full_text],
            metadatas=[{"author": author, "title": title}]
        )
        return "Idea successfully saved to the Global Mesh!"

    def search_similar(self, query: str):
        results = self.vector_db.similarity_search(query, k=3)
        matches = []
        for r in results:
            matches.append({"title": r.metadata.get('title', 'Unknown'), "author": r.metadata.get('author', 'Unknown'), "idea": r.page_content})
        return matches
