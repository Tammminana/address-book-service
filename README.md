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
- **Strict API Contract**: Follows the provided API specification for seamless integration and testing.

## Prerequisites

- Python 3.8+
```bash
    python --version
    ```

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
Also swagger UI for interactive usage of apis available at `http://127.0.0.1:5000/docs`.
and API documentation at `http://127.0.0.1:5000/redoc`.

## API Usage (cURL Examples)

You can interact with the API using any HTTP client like `cURL` or Postman.

### 1. Create Contact(s)

```bash
curl -X POST "\http://127.0.0.1:5000/create" \
-H "Content-Type: application/json" \
-d '[
    {
        "name": "Alice Smith",
        "phone": "1234567890",
        "email": "alice@example.com"
    },
    {
        "name": "Bob Jones",
        "phone": "2345678901",
        "email": "bob@example.com"
    }
]'
```

### 2. Update Contact(s)
*(Replace `"your-uuid-here"` with an actual ID from the create response)*
```bash
curl -X PUT "http://127.0.0.1:5000/update" \
-H "Content-Type: application/json" \
-d '[
    {
        "id": "your-uuid-for-alice",
        "phone": "9999999999"
    }
]'
```

### 3. Search Contact(s)
```bash
curl -X POST "http://127.0.0.1:5000/search" \
-H "Content-Type: application/json" \
-d '{
    "query": "smith"
}'
```

### 4. Delete Contact(s)
*(Replace with actual IDs)*
```bash
curl -X DELETE "http://127.0.0.1:5000/delete" \
-H "Content-Type: application/json" \
-d '[
    "your-uuid-for-alice",
    "your-uuid-for-bob"
]'
```


### Issues Faced and Resolved During Setup
This section outlines common issues that might be encountered during the setup process and their respective solutions.

#### 1. pip._vendor.pep517.wrappers.BackendUnavailable or Pip Version Warning
Issue:
You might encounter an error like pip._vendor.pep517.wrappers.BackendUnavailable or a warning about an outdated pip version, such as:

```bash
return self._call_hook('get_requires_for_build_wheel', {
  File "/home/narsingh/core/interview/urbancompany/address-book-service/venv/lib/python3.8/site-packages/pip/_vendor/pep517/wrappers.py", line 162, in _call_hook
    raise BackendUnavailable
pip._vendor.pep517.wrappers.BackendUnavailable

WARNING: You are using pip version 19.2.3, however version 25.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command
```

Resolution:
This typically indicates an outdated pip version. Upgrade pip to the latest version within your virtual environment:

```bash
pip install --upgrade pip
```


#### 2. TypeError: 'type' object is not subscriptable (Python Version Incompatibility)
This error occurs when using type hints like set[str] or Contact | None in Python versions older than 3.9 (for generic types like set) or 3.10 (for the | union operator).

Example error: 
```bash
File "/home/narsingh/core/interview/urbancompany/address-book-service/address_book/storage/in_memory.py", line 17, in InMemoryStorage
    def _get_index_words(self, text: str) -> set[str]:
TypeError: 'type' object is not subscriptable
```

Resolution:
The recommended solution is to upgrade your Python version to 3.8.0 or newer. If you are in a virtual environment, you will need to create a new virtual environment with the desired Python version.