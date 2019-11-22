from unittest import TestCase
from transaction import Transaction


class TestTransaction(TestCase):
    def tearDown(self) -> None:
        pass

    def test_get_sum_time_of_save_and_all_data(self):
        # given
        transaction = Transaction()

        # when
        actual_sum_time = transaction.get_sum_time(is_save_to_disc=True, is_useful_data_only=False)

        # then
        expected_transfer_time = transaction.data_amount * 2 + 10
        expected_persist_time = transaction.data_amount * 5 + 40
        expected_sum_time = transaction.transaction_time + expected_transfer_time + expected_persist_time
        self.assertAlmostEquals(expected_sum_time, actual_sum_time, delta=0.0001)

    def test_get_sum_time_of_save_and_useful_data(self):
        # given
        transaction = Transaction()

        # when
        actual_sum_time = transaction.get_sum_time(is_save_to_disc=True, is_useful_data_only=True)

        # then
        expected_transfer_time = transaction.useful_data_amount * 2 + 10
        expected_persist_time = transaction.useful_data_amount * 5 + 40
        expected_sum_time = transaction.transaction_time + expected_transfer_time + expected_persist_time
        self.assertAlmostEquals(expected_sum_time, actual_sum_time, delta=0.0001)

    def test_get_sum_time_of_not_save_and_useful_data(self):
        # given
        transaction = Transaction()

        # when
        actual_sum_time = transaction.get_sum_time(is_save_to_disc=False, is_useful_data_only=True)

        # then
        expected_transfer_time = transaction.useful_data_amount * 2 + 10
        expected_sum_time = transaction.transaction_time + expected_transfer_time
        self.assertAlmostEquals(expected_sum_time, actual_sum_time, delta=0.0001)

    def test_get_sum_time_of_not_save_and_all(self):
        # given
        transaction = Transaction()

        # when
        actual_sum_time = transaction.get_sum_time(is_save_to_disc=False, is_useful_data_only=False)

        # then
        expected_transfer_time = transaction.data_amount * 2 + 10
        expected_sum_time = transaction.transaction_time + expected_transfer_time
        self.assertAlmostEquals(expected_sum_time, actual_sum_time, delta=0.0001)
