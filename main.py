# to build APIs
from fastapi import FastAPI
from address_book.api import endpoints
# server required to run an asynchronous framework
import uvicorn

app = FastAPI(
    title="Address Book Service",
    description="A modular, in-memory address book API.",
    version="1.0.0"
)

# API router
app.include_router(endpoints.router)

@app.get("/", tags=["Health Check"])
# this is the root endpoint for health check
def read_root():
    return {"status": "ok", "message": "Address Book service is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)