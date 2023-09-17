import abc

from data.model.diary import Diary


class DiaryRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, diary: Diary) -> Diary:
        pass

    @abc.abstractmethod
    def delete(self, diary: Diary):
        pass

    @abc.abstractmethod
    def find_by_id(self, i_d: int) -> Diary:
        pass

    @abc.abstractmethod
    def find_all(self) -> list[Diary]:
        pass

    @abc.abstractmethod
    def count(self) -> int:
        pass

    @abc.abstractmethod
    def clear(self) -> None:
        pass
