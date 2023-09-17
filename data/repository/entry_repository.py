import abc

from data.model.entry import Entry


class EntryRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, entry: Entry) -> Entry:
        pass

    @abc.abstractmethod
    def delete(self, entry: Entry):
        pass

    @abc.abstractmethod
    def find_by_id(self, i_d: int) -> Entry:
        pass

    @abc.abstractmethod
    def find_all(self) -> list[Entry]:
        pass

    @abc.abstractmethod
    def count(self) -> int:
        pass

    @abc.abstractmethod
    def clear(self) -> None:
        pass
