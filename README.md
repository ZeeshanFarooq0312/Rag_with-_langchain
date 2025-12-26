# RAG Lang Chain Project

A Retrieval-Augmented Generation (RAG) system that loads PDF documents, processes them using LangChain, creates embeddings, and generates intelligent responses using OpenAI's GPT API.

## Features

- **PDF Document Loading**: Load and parse PDF files using PyPDFLoader
- **Text Splitting**: Intelligently chunk documents using RecursiveCharacterTextSplitter
- **Embeddings**: Generate vector embeddings using OpenAI's embedding models
- **Vector Store**: Store and retrieve documents using FAISS (Facebook AI Similarity Search)
- **RAG Pipeline**: Query documents and generate contextual responses using GPT-3.5-turbo
- **Context-Aware Responses**: Generate 3-line summaries from document context

## Prerequisites

- Python 3.11+
- OpenAI API key

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd d:\personal_projects\Rag_Lang_Chain
   ```

2. **Create and activate a virtual environment** (if not already done):
   ```bash
   python -m venv venv
   venv\Scripts\Activate.ps1  # On Windows PowerShell
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Additional packages** (if not in requirements.txt):
   ```bash
   pip install langchain langchain-community langchain-text-splitters langchain-openai langchain-embeddings faiss-cpu openai python-dotenv pypdf
   ```

## Configuration

### Environment Setup

1. **Create a `.env` file** in the project root:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

2. **Alternatively, set the environment variable in PowerShell**:
   ```powershell
   $env:OPENAI_API_KEY="sk-..."
   ```

## Usage

### Basic Setup

Edit the file path in `main.py`:
```python
file_path = r"D:\personal_projects\Rag_Lang_Chain\Your_PDF_File.pdf"
```

### Run the Script

```bash
python main.py
```

### Customize the Query

Modify the query in the `if __name__ == "__main__":` block:
```python
query = "Your question here?"
```

## Project Structure

```
.
├── main.py                 # Main RAG pipeline script
├── requirements.txt        # Project dependencies
├── README.md              # This file
└── faiss_index/           # FAISS vector store (created after first run)
```

## How It Works

1. **Load PDF**: Extracts text from PDF documents
2. **Split Text**: Chunks documents into 1000-character segments with 200-character overlap
3. **Create Embeddings**: Converts text chunks into vector embeddings using OpenAI
4. **Store in FAISS**: Indexes embeddings for fast similarity search
5. **Query & Retrieve**: Finds the 5 most relevant document chunks for a query
6. **Generate Response**: Uses GPT-3.5-turbo to create a contextual 3-line summary

## Configuration Options

Adjust these parameters in the functions:

- **chunk_size**: Document chunk size (default: 1000 characters)
- **chunk_overlap**: Overlap between chunks (default: 200 characters)
- **k**: Number of results to retrieve (default: 5)
- **model**: LLM model to use (default: gpt-3.5-turbo)

## Dependencies

Key packages:
- `langchain-community`: Document loaders and vector stores
- `langchain-text-splitters`: Text splitting utilities
- `langchain-openai`: OpenAI integration
- `faiss-cpu`: Vector similarity search
- `openai`: Official OpenAI Python client
- `pypdf`: PDF parsing
- `python-dotenv`: Environment variable management

## Troubleshooting

### ModuleNotFoundError
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### OpenAI API Error
- Verify `OPENAI_API_KEY` is set correctly
- Check that your API key is valid and has access to embeddings and chat endpoints

### FAISS Import Error
Install the CPU version:
```bash
pip install faiss-cpu
```

### Python 3.14+ Pydantic Warning
This is a known compatibility warning and won't affect functionality.

## Future Enhancements

- Add support for multiple file formats (DOCX, TXT)
- Implement chat history and conversation memory
- Add batch processing for large document sets
- Support for different embedding models
- Web interface with Flask/FastAPI

## License

Open source

## Notes

- The system generates FAISS indices locally for faster subsequent queries
- Responses are limited to out-of-context detection ("its out of document question")
- API costs depend on OpenAI usage for embeddings and chat completions
