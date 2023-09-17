from unittest import TestCase

from data.model.diary import Diary
from data.repository import diary_repository_impl


class TestCaseDiaryRepositoryImpl(TestCase):
    def setUp(self) -> None:
        self.diaryRepository = diary_repository_impl.DiaryRepositoryImpl()

    def test_that_one_diary_can_be_saved(self):
        self.diary = Diary()
        self.diaryRepository.save(self.diary)
        self.assertEqual(1, self.diaryRepository.count())

    def test_that_one_diary_can_be_saved_and_can_be_found(self):
        self.diary = Diary()
        self.diary.set_username('esther')
        self.diaryRepository.save(self.diary)

        self.assertEqual(1, self.diaryRepository.count())
        self.assertEqual('esther', self.diaryRepository.find_by_id(1).get_username())

    def test_that_one_diary_can_be_saved_and_updated(self):
        self.diary = Diary()
        self.diary.set_username('esther')
        self.diaryRepository.save(self.diary)

        self.assertEqual(1, self.diaryRepository.count())
        self.diary.set_id(1)
        self.diary.set_username('adunni')
        self.diaryRepository.save(self.diary)

        self.assertEqual('adunni', self.diaryRepository.find_by_id(1).get_username())

    def test_that_the_list_of_diaries_can_printed_out(self):
        self.diary1 = Diary()
        self.diary1.set_username('esther')
        self.diaryRepository.save(self.diary1)

        self.diary2 = Diary()
        self.diary2.set_username('adunni')
        self.diaryRepository.save(self.diary2)

        self.diary3 = Diary()
        self.diary3.set_username('deborah')
        self.diaryRepository.save(self.diary3)

        self.assertEqual(3, self.diaryRepository.count())

        self.assertEqual('esther', self.diaryRepository.find_by_id(1).get_username())
        self.assertEqual('adunni', self.diaryRepository.find_by_id(2).get_username())
        self.assertEqual('deborah', self.diaryRepository.find_by_id(3).get_username())

        expected_diaries = [self.diary1, self.diary2, self.diary3]
        self.assertEqual(expected_diaries, self.diaryRepository.find_all())

    def test_that_the_a_diary_can_be_deleted_from_the_list_of_diaries(self):
        self.diary1 = Diary()
        self.diary1.set_username('esther')
        self.diaryRepository.save(self.diary1)

        self.diary2 = Diary()
        self.diary2.set_username('adunni')
        self.diaryRepository.save(self.diary2)

        self.diary3 = Diary()
        self.diary3.set_username('deborah')
        self.diaryRepository.save(self.diary3)

        self.assertEqual(3, self.diaryRepository.count())

        self.assertEqual('esther', self.diaryRepository.find_by_id(1).get_username())
        self.assertEqual('adunni', self.diaryRepository.find_by_id(2).get_username())
        self.assertEqual('deborah', self.diaryRepository.find_by_id(3).get_username())

        self.diaryRepository.delete(self.diary1)
        self.assertIsNone(self.diaryRepository.find_by_id(1))

    def test_that_the_list_of_diaries_can_be_cleared(self):
        self.diary1 = Diary()
        self.diary1.set_username('esther')
        self.diaryRepository.save(self.diary1)

        self.diary2 = Diary()
        self.diary2.set_username('adunni')
        self.diaryRepository.save(self.diary2)

        self.diary3 = Diary()
        self.diary3.set_username('deborah')
        self.diaryRepository.save(self.diary3)

        self.assertEqual(3, self.diaryRepository.count())

        self.assertEqual('esther', self.diaryRepository.find_by_id(1).get_username())
        self.assertEqual('adunni', self.diaryRepository.find_by_id(2).get_username())
        self.assertEqual('deborah', self.diaryRepository.find_by_id(3).get_username())

        self.diaryRepository.clear()
        self.assertEqual(0, self.diaryRepository.count())

