from unittest import TestCase
from transaction import Transaction
from distributed_transaction import DistributedTransaction


class TestDistributedTransaction(TestCase):
    def given_transaction_summary_time_will_return(self, transaction: Transaction, is_save_to_disc: bool,
                                                   is_useful_data_only: bool, time: float) -> None:
        transaction.get_time = lambda save_to_disc, useful_data_only: \
            time if (is_save_to_disc == save_to_disc) & (is_useful_data_only == useful_data_only) else self.fail()

    def setUp(self) -> None:
        pass

    def test_summary_transaction_time_of_empty_will_return_null(self):
        # given
        transaction = DistributedTransaction([])

        # when
        actual_sum = transaction.summary_transaction_time(True, True)

        # then
        self.assertEqual(0, actual_sum)

    def test_summary_transaction_time_of_few_transactions_will_return_sum_of_their_sum_time(self):
        # given
        transaction1 = Transaction()
        self.given_transaction_summary_time_will_return(transaction1, True, False, 5)
        transaction2 = Transaction()
        self.given_transaction_summary_time_will_return(transaction2, True, False, 7)

        transaction = DistributedTransaction([transaction1, transaction2])

        # when
        actual_sum = transaction.summary_transaction_time(True, False)

        # then
        self.assertEqual(12, actual_sum)

    def test_summary_transaction_time_of_one_transaction_will_return_sum_of_it_sum_time(self):
        # given
        transaction1 = Transaction()
        self.given_transaction_summary_time_will_return(transaction1, False, True, 5)

        transaction = DistributedTransaction([transaction1])

        # when
        actual_sum = transaction.summary_transaction_time(False, True)

        # then
        self.assertEqual(5, actual_sum)
