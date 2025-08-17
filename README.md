# Basic RAG

## Abstract
This is a basic CLI Based RAG System.
**Step 1:** data/.md file → loader → chunk → embedding → vector db \
**Step 2:** query → retriever → prompt → LLM → parser


## Features
- Single file type: Markdown (.md)
- Unstructured data
- No memory (stateless Q&A)
- Local vector store with persistence


## Tech Stack
- Python - **Programming Language**
- LangChain - **Gen AI Framework** 
- Chroma - **Vector DB**
- Hugging Face - **API Access Token**


## How It Works
1. Preprocessing (**ingest.py**)
    - Loads Markdown files from DATA_DIRECTORY_ABSOLUTE_PATH using `DirectoryLoader` and `UnstructuredMarkdownLoader`.
    - Splits content into overlapping chunks (`chunk_size`, `chunk_overlap`) with `RecursiveCharacterTextSplitter`.
    - Embeds chunks via `HuggingFaceEmbeddings` (EMBEDDING_MODEL_REPO_ID).
    - Persists vectors to a local Chroma DB at VECTOR_DB_PERSISTENT_ABSOLUTE_PATH, under collection VECTOR_DB_NAME.

2. Retrieval + Generation (**pipeline.py**)
    - Reconnects to the same Chroma store using the same embedding model.
    - Creates a retriever (similarity).
    - Formats a concise prompt with retrieved context.
    - Calls a Hugging Face Inference endpoint model (CHAT_MODEL_REPO_ID) to generate a compact answer.
    - Returns a 2–3 line response.

3. CLI App (**main.py**)
    - A simple REPL loop to enter questions.
    - Type **exit** to quit.


## Installation
1. Install Python: Ensure Python is installed matching the version in .python-version. 
2. Install UV (Python package manager) **Globally** - `pip install uv`
3. Clone the repository
    - git clone https://github.com/amitmahapatrav5/rag-qna-01-unstructured-single.git
    - cd <repo-directory>
4. Install dependencies `uv sync`


## Environment Setup
1. Create a Hugging Face API key
    - Edit Permission and enable below 2 permissions
        - **Read access to contents of all public gated repos you can access**
        - **Make calls to Inference Providers**

2. Prepare .env
    - Copy **.env.example** and rename it to **.env**.
    - Fill in all the required variables.

3. Prepare data
    - Place one or more .md files in any local folder.
    - Use the absolute path of that folder in the environment variable below.


## Customization In Code
- Chunking
    - chunk_size
    - chunk_overlap
- Retrieval type/depth
    - search_type
    - k
- Prompting style
    - Modify the PromptTemplate in pipeline.py to fit desired tone/length or to include citations.


## Run Sequence with Example

- uv run python ingest.py
- uv run python main.py
- Query: What topics are covered in the docs?
- Answer: A concise 2–3 line response grounded in the ingested Markdown.
- Type exit to stop.