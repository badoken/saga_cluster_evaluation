from unittest import TestCase

from distributed_transaction_factory import DistributedTransactionFactory
from transaction import Transaction


class TestDistributedTransactionFactory(TestCase):
    def test_generate_if_positive_value_specified(self):
        # given
        factory = DistributedTransactionFactory(replication_factor=3)

        # when
        distributed_transaction = factory.generate(4)

        # then
        self.assertEqual(4, len(distributed_transaction.local_transactions))
        self.assertEqual(3, distributed_transaction.replication_factor)
        for transaction in distributed_transaction.local_transactions:
            self.assertIsInstance(transaction, Transaction)

    def test_generate_if_negative_value_specified(self):
        # given
        factory = DistributedTransactionFactory()

        # when
        actual = None
        try:
            distributed_transaction = factory.generate(-1)
        except ValueError as error:
            actual = error

        # then
        self.assertIsNotNone(actual)
