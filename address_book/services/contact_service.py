import uuid
from typing import List

from address_book.models.contact import Contact, ContactCreate, ContactUpdate
from address_book.storage.in_memory import InMemoryStorage, storage_instance

class ContactService:
    def __init__(self, storage: InMemoryStorage):
        self.storage = storage

    def create_contacts(self, contacts_data: List[ContactCreate]) -> List[Contact]:
        created_contacts = []
        for contact_data in contacts_data:
            new_contact = Contact(**contact_data.dict())
            created_contact = self.storage.create(new_contact)
            created_contacts.append(created_contact)
        # this returns all the created contacts
        return created_contacts

    def update_contacts(self, updates: List[ContactUpdate]) -> List[Contact]:
        updated_contacts = []
        for update_data in updates:
            updated_contact = self.storage.update(update_data)
            if updated_contact:
                updated_contacts.append(updated_contact)
        # returns all the updated contacts in the response
        return updated_contacts

    def delete_contacts(self, contact_ids: List[uuid.UUID]) -> int:
        deleted_count = 0
        for contact_id in contact_ids:
            if self.storage.delete(contact_id):
                deleted_count += 1
        # this just returns the coutn of the deleted contacts frpm the address book
        return deleted_count

    def search_contacts(self, query: str) -> List[Contact]:
        matching_ids = self.storage.search(query)
        return [self.storage.get_by_id(cid) for cid in matching_ids if self.storage.get_by_id(cid)]

# Service instance using the singleton storage
contact_service_instance = ContactService(storage=storage_instance)