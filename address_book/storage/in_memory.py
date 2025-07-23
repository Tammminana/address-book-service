import re
import uuid
from collections import defaultdict
from typing import Set
from typing import Optional

from address_book.models.contact import Contact, ContactUpdate

# This class is designed as a singleton, instantiated once and shared.
class InMemoryStorage:
    def __init__(self):
        # this is for storing contacts
        self.contacts_db: dict[uuid.UUID, Contact] = {}
        # this is for search index
        self.search_index: dict[str, Set[uuid.UUID]] = defaultdict(set)

    # here function splits text into normalized words for indexing.
    def _get_index_words(self, text: str) -> Set[str]:
        if not text:
            return set()
        # split by common delimiters(ex: .,@ etc) and convert to lowercase
        return set(re.split(r'[\s,@.]+', text.lower()))

    # adds a contact to the search index.
    def _index_contact(self, contact: Contact):
        words_to_index = self._get_index_words(contact.name) | self._get_index_words(contact.email)
        for word in words_to_index:
            if word: # to avoid indexing empty strings
                self.search_index[word].add(contact.id)

    # removes a contact from the search index.
    def _deindex_contact(self, contact: Contact):
        words_to_deindex = self._get_index_words(contact.name) | self._get_index_words(contact.email)
        for word in words_to_deindex:
            if word in self.search_index:
                self.search_index[word].discard(contact.id)
                if not self.search_index[word]: 
                    del self.search_index[word]

    # create a contact in the inMemory
    def create(self, contact: Contact) -> Contact:
        self.contacts_db[contact.id] = contact
        self._index_contact(contact)
        return contact

    # get contact object by id
    def get_by_id(self, contact_id: uuid.UUID) -> Optional[Contact]:
        return self.contacts_db.get(contact_id)

    # update contact by id
    def update(self, update_data: ContactUpdate) -> Optional[Contact]:
        contact_to_update = self.get_by_id(update_data.id)
        if not contact_to_update:
            return None

        # de-index the old data
        self._deindex_contact(contact_to_update)

        # update contact with new data
        update_dict = update_data.dict(exclude_unset=True)
        updated_contact = contact_to_update.copy(update=update_dict)
        self.contacts_db[updated_contact.id] = updated_contact

        # re-index with new data
        self._index_contact(updated_contact)
        return updated_contact

    def delete(self, contact_id: uuid.UUID) -> bool:
        contact_to_delete = self.get_by_id(contact_id)
        if not contact_to_delete:
            return False

        self._deindex_contact(contact_to_delete)
        del self.contacts_db[contact_id]
        return True

    def search(self, query: str) -> Set[uuid.UUID]:
        normalized_query = query.lower()
        return self.search_index.get(normalized_query, set())

# creating a single instance to be used across the application
storage_instance = InMemoryStorage()