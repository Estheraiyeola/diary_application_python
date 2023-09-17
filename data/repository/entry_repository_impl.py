from data.model.entry import Entry
from data.repository.entry_repository import EntryRepository


class EntryRepositoryImpl(EntryRepository):
    def __init__(self):
        self.entries = []
        self.counter = 0

    def save(self, entry: Entry) -> Entry:
        entry_does_not_exists = entry.get_id() == 0
        if entry_does_not_exists:
            self.save_new(entry)
            self.counter += 1
        else:
            self.update(entry)
        return entry

    def delete(self, entry: Entry):
        self.entries.remove(entry)

    def find_by_id(self, i_d: int) -> Entry:
        for entry in self.entries:
            if entry.get_id() == i_d:
                return entry

    def find_all(self) -> list[Entry]:
        return self.entries

    def count(self) -> int:
        return self.counter

    def clear(self) -> None:
        self.counter -= len(self.entries)
        self.entries.clear()

    def save_new(self, entry):
        entry.set_id(self.generate_id())
        self.entries.append(entry)

    def update(self, entry):
        updated_entry = self.find_by_id(entry.get_id())
        updated_entry.set_title(entry.get_title())
        updated_entry.set_body(entry.get_body())

    def generate_id(self):
        return self.counter + 1
