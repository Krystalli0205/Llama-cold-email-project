import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator for Kiki.ai 📧 ")
    url_input = st.text_input("Enter a job postingURL:", value="https://jobs.nike.com/job/R-47330?from=job%20search%20funnel")
    submit_button = st.button("Submit")

    # the following code is to be run when the submit button is clicked
    # it will load the website, clean the text, extract the skills wanted, load the most relevant portfolio items from the database, and write the email
    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

# the following code will create the chain, portfolio, and set the page config
if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title=" Cold Mail Generator for Kiki.ai 📧 ", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)

