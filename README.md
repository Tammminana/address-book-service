# Modular Address Book Service

This project is a modular, in-memory Address Book service built with Python and FastAPI. It supports creating, updating, deleting, and searching contacts with a focus on performance and scalability.

## Design Highlights

- **In-Memory Storage**: Uses Python dictionaries for `O(1)` average-time complexity on key-based operations.
- **Optimized Search**: Implements an inverted index for fast, `O(1)` lookups on search terms.
- **Modular Architecture**: Code is separated into distinct layers:
    - **API/Controllers**: Manages HTTP endpoints.
    - **Services**: Contains the core business logic.
    - **Storage**: Encapsulates data structures and access patterns.
    - **Models**: Defines data schemas using Pydantic.

## Prerequisites

- Python 3.8+

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd address-book-service
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Service

To start the API server, run the following command from the root directory (`address-book-service/`):

```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```
The service will be available at `http://127.0.0.1:5000`.