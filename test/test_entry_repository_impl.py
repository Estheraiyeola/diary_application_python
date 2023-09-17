from unittest import TestCase

from data.model.entry import Entry
from data.repository.entry_repository_impl import EntryRepositoryImpl


class TestCaseForEntryRepository(TestCase):
    def setUp(self) -> None:
        self.entry_repository = EntryRepositoryImpl()

    def test_that_one_entry_can_be_saved(self):
        self.entry = Entry()
        self.entry_repository.save(self.entry)
        self.assertEqual(1, self.entry_repository.count())

    def test_that_one_entry_can_be_saved_and_can_be_found(self):
        self.entry = Entry()
        self.entry.set_title('title')
        self.entry.set_title('body')
        self.entry_repository.save(self.entry)

        self.assertEqual(1, self.entry_repository.count())
        self.assertEqual(self.entry, self.entry_repository.find_by_id(1))

    def test_that_one_entry_can_be_saved_and_can_be_updated(self):
        self.entry = Entry()
        self.entry.set_title('title')
        self.entry.set_body('body')
        self.entry_repository.save(self.entry)

        self.assertEqual(1, self.entry_repository.count())
        self.assertEqual(self.entry, self.entry_repository.find_by_id(1))

        self.entry.set_id(1)
        self.entry.set_title('Title')
        self.entry.set_body('Body')
        self.entry_repository.save(self.entry)

        self.assertEqual('Title', self.entry_repository.find_by_id(1).get_title())
        self.assertEqual('Body', self.entry_repository.find_by_id(1).get_body())

    def test_that_entries_can_be_saved_and_can_all_be_printed(self):
        self.entry = Entry()
        self.entry.set_title('title')
        self.entry.set_body('body')
        self.entry_repository.save(self.entry)

        self.assertEqual(1, self.entry_repository.count())
        self.assertEqual(self.entry, self.entry_repository.find_by_id(1))

        self.entry1 = Entry()
        self.entry1.set_title('Title')
        self.entry1.set_body('Body')
        self.entry_repository.save(self.entry1)

        self.assertEqual(2, self.entry_repository.count())
        self.assertEqual(self.entry1, self.entry_repository.find_by_id(2))

        self.assertEqual('title', self.entry_repository.find_by_id(1).get_title())
        self.assertEqual('body', self.entry_repository.find_by_id(1).get_body())

        self.assertEqual('Title', self.entry_repository.find_by_id(2).get_title())
        self.assertEqual('Body', self.entry_repository.find_by_id(2).get_body())

        expected_entries = [self.entry, self.entry1]
        self.assertEqual(expected_entries, self.entry_repository.find_all())

    def test_that_an_entry_can_be_deleted(self):
        self.entry = Entry()
        self.entry.set_title('title')
        self.entry.set_body('body')
        self.entry_repository.save(self.entry)

        self.assertEqual(1, self.entry_repository.count())
        self.assertEqual(self.entry, self.entry_repository.find_by_id(1))

        self.entry1 = Entry()
        self.entry1.set_title('Title')
        self.entry1.set_body('Body')
        self.entry_repository.save(self.entry1)

        self.assertEqual(2, self.entry_repository.count())
        self.assertEqual(self.entry1, self.entry_repository.find_by_id(2))

        self.assertEqual('title', self.entry_repository.find_by_id(1).get_title())
        self.assertEqual('body', self.entry_repository.find_by_id(1).get_body())

        self.assertEqual('Title', self.entry_repository.find_by_id(2).get_title())
        self.assertEqual('Body', self.entry_repository.find_by_id(2).get_body())

        self.entry_repository.delete(self.entry)
        self.assertIsNone(self.entry_repository.find_by_id(1))

    def test_that_all_entries_can_be_deleted(self):
        self.entry = Entry()
        self.entry.set_title('title')
        self.entry.set_body('body')
        self.entry_repository.save(self.entry)

        self.assertEqual(1, self.entry_repository.count())
        self.assertEqual(self.entry, self.entry_repository.find_by_id(1))

        self.entry1 = Entry()
        self.entry1.set_title('Title')
        self.entry1.set_body('Body')
        self.entry_repository.save(self.entry1)

        self.assertEqual(2, self.entry_repository.count())
        self.assertEqual(self.entry1, self.entry_repository.find_by_id(2))

        self.assertEqual('title', self.entry_repository.find_by_id(1).get_title())
        self.assertEqual('body', self.entry_repository.find_by_id(1).get_body())

        self.assertEqual('Title', self.entry_repository.find_by_id(2).get_title())
        self.assertEqual('Body', self.entry_repository.find_by_id(2).get_body())

        self.entry_repository.clear()
        self.assertIsNone(self.entry_repository.find_by_id(1))

