# Llama-cold-email-project
The project is designed for HR firms managing skilled contractors from regions like India and Indonesia, offering big tech companies a cost-effective solution for filling specialized tech roles. Using Llama3.1 and LangChain, this app automates email generation by extracting job requirements from company career pages, matching required skills with contractor portfolios, and crafting personalized, compelling emails. 

---

## Table of Contents
1. [Business Problem](#business-problem)
2. [Target Users](#target-users)
3. [Tool Purpose](#tool-purpose)
4. [Technical Architecture](#technical-architecture)
5. [Model](#model)
6. [Notebook Testing](#notebook-testing)
7. [App Components](#app-components)
8. [Setup Instructions](#setup-instructions)
9. [Usage](#usage)
10. [Questions](#questions)

---

## Business Problem

Large companies face challenges filling specialized tech roles due to high costs and limited local talent. Many are open to hiring remote, cost-effective alternatives, provided they match the required skills.

## Target Users

This tool is built for HR outsourcing firms that manage tech contractors from regions with competitive labor costs, like India and Indonesia. These firms offer professionals in roles such as software engineering and data analysis.

## Tool Purpose

The tool automates and personalizes cold outreach emails using Llama3.1. By extracting job requirements from large companies' career pages, matching them with contractor portfolios, and crafting customized emails, it allows HR firms to highlight cost savings and skill alignment to hiring managers.

---

## Technical Architecture

1. **Extract Job Posting Text**: Use LangChain to scrape job descriptions from company career pages.
2. **LLM Processing**: Convert job descriptions into structured JSON format with fields like `role`, `experience`, `skills`, and `description`.
3. **Database Matching**: Use ChromaDB to store and query contractor portfolios by skills.
4. **Email Generation**: Generate cold outreach emails by combining job requirements and matching contractor profiles.

---

## Model

- **Llama3.1**: Used for natural language processing tasks. Hosted on Groq.cloud to speed up inference time with the Llama-70b-8192 model. Requires an API key for Groq.
  
---

## Testing using Jupyter Notebook

1. **LLM Test**: Verify LLM functionality using LangChain for ease of LLM application development.
2. **Vector DB Test**: ChromaDB serves as a lightweight, open-source vector database.
3. **Text Extraction**: Scrape and format job postings from web pages.
4. **ChromaDB Setup**: Store and query contractor portfolios.
5. **Email Generation**: Customize prompts for creating targeted, effective cold emails.

---

## Complete App Components

1. **[main.py]**: Streamlit-based UI for entering job posting URLs and generating emails.
2. **[chain.py]**: LLM application with API key handling via `.env`.
3. **[portfolio.py]**: ChromaDB setup to manage contractor portfolios.
4. **[utils.py]**: Text processing functions for cleaner, more readable emails.
