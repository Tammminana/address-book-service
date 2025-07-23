import uuid
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# base model with common contact fields
class ContactBase(BaseModel):
    name: str
    phone: str
    email: EmailStr

# to create a contact using the request body
class ContactCreate(ContactBase):
    pass

# full data from the contact
class Contact(ContactBase):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    class Config:
        from_attributes = True

# update the contact
class ContactUpdate(BaseModel):
    id: uuid.UUID
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None

# searching in the address book
class SearchRequest(BaseModel):
    query: str