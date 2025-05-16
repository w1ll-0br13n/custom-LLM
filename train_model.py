import os
import glob
from typing import List, Optional
from langchain.text_splitter import MarkdownTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv

class ProjectAI:
    def __init__(self, docs_dir: str, db_dir: str = "db"):
        self.docs_dir = docs_dir
        self.db_dir = db_dir
        self.embeddings = HuggingFaceEmbeddings()
        self.vector_store = None
        self.qa_chain = None

    def load_documents(self) -> List[str]:
        """Load all markdown files from the documentation directory."""
        markdown_files = glob.glob(os.path.join(self.docs_dir, "**/*.md"), recursive=True)
        documents = []
        for file_path in markdown_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                documents.append(f.read())
        return documents

    def process_documents(self, documents: List[str]):
        """Process and split documents into chunks for training."""
        text_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = []
        for doc in documents:
            splits.extend(text_splitter.split_text(doc))
        return splits

    def create_vector_store(self, splits: List[str]):
        """Create and persist vector store from document chunks."""
        self.vector_store = Chroma.from_texts(
            texts=splits,
            embedding=self.embeddings,
            persist_directory=self.db_dir
        )
        self.vector_store.persist()

    def setup_qa_chain(self):
        """Initialize the QA chain with the vector store."""
        load_dotenv()
        llm = HuggingFaceHub(
            repo_id="google/flan-t5-base",
            model_kwargs={"temperature": 0.5, "max_length": 512}
        )
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever()
        )

    def query(self, question: str) -> str:
        """Process a query and return an answer based on the documentation."""
        if not self.qa_chain:
            return "Error: Model not initialized. Please train the model first."

        try:
            result = self.qa_chain.run(question)
            # Check if the answer is relevant to the project scope
            if not result or len(result.strip()) < 10:
                return "I apologize, but this question appears to be outside the scope of the project documentation."
            return result
        except Exception as e:
            return f"Error processing query: {str(e)}"

    def train(self):
        """Main training pipeline."""
        print("Loading documents...")
        documents = self.load_documents()
        if not documents:
            raise ValueError("No markdown documents found in the specified directory.")

        print("Processing documents...")
        splits = self.process_documents(documents)

        print("Creating vector store...")
        self.create_vector_store(splits)

        print("Setting up QA chain...")
        self.setup_qa_chain()

        print("Training complete!")

def main():
    # Initialize and train the model
    project_ai = ProjectAI(docs_dir="docs")
    try:
        project_ai.train()
        print("\nModel is ready for queries!")
        
        # Interactive query loop
        while True:
            question = input("\nEnter your question (or 'quit' to exit): ")
            if question.lower() == 'quit':
                break
            answer = project_ai.query(question)
            print(f"\nAnswer: {answer}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()