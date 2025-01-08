import pandas as pd
import chromadb
import uuid


class Portfolio:
    # initialize the portfolio
    def __init__(self, file_path="/Users/krystalli/Documents/cold-email-project/app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore') 
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio") 

    # load the portfolio into the vector store
    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    # query the most relevant portfolio items
    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])