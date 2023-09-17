from data.model.diary import Diary
from data.repository.diary_repository import DiaryRepository


class DiaryRepositoryImpl(DiaryRepository):

    def __init__(self):
        self.diaries = []
        self.counter = 0

    def save(self, diary: Diary) -> Diary:
        diary_does_not_exist = diary.get_id() == 0
        if diary_does_not_exist:
            self.save_new(diary)
            self.counter += 1
        else:
            self.update(diary)
        return diary

    def delete(self, diary: Diary):
        self.diaries.remove(diary)

    def find_by_id(self, i_d: int) -> Diary:
        for diary in self.diaries:
            if diary.get_id() == i_d:
                return diary

    def find_all(self) -> list[Diary]:
        return self.diaries

    def count(self) -> int:
        return self.counter

    def clear(self) -> None:
        self.counter -= len(self.diaries)
        self.diaries.clear()

    def save_new(self, diary):
        diary.set_id(self.generate_id())
        self.diaries.append(diary)
        self.count()

    def update(self, diary):
        updated_diary = self.find_by_id(diary.get_id())
        updated_diary.set_username(diary.get_username())

    def generate_id(self):
        return self.counter + 1
