import uuid
from typing import List
from fastapi import APIRouter, HTTPException, status

from address_book.models.contact import Contact, ContactCreate, ContactUpdate, SearchRequest
from address_book.services.contact_service import contact_service_instance

router = APIRouter()

@router.post("/create", response_model=List[Contact], status_code=status.HTTP_201_CREATED)
# this creates 1 or more new contacts
def create_contacts(contacts_data: List[ContactCreate]):
    return contact_service_instance.create_contacts(contacts_data)

@router.put("/update", response_model=List[Contact])
# this updates 1 or more existing contacts based on their ID
def update_contacts(updates: List[ContactUpdate]):
    updated_contacts = contact_service_instance.update_contacts(updates)
    return updated_contacts

@router.delete("/delete", response_model=dict)
# deletes a contact by the given ids
def delete_contacts(contact_ids: List[uuid.UUID]):
    deleted_count = contact_service_instance.delete_contacts(contact_ids)
    return {"deleted": deleted_count}

@router.post("/search", response_model=List[Contact])
# typical search based on the query string in the name or email present in the contact
def search_contacts(search_request: SearchRequest):
    if not search_request.query.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query cannot be empty."
        )
    return contact_service_instance.search_contacts(search_request.query)