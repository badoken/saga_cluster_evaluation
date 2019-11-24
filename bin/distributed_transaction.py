from dataclasses import dataclass
from transaction import Transaction
from functional import seq


@dataclass
class DistributedTransaction:
    local_transactions: [Transaction]
    replication_factor: int = 1

    def summary_transaction_time(self, is_save_to_disc: bool, is_useful_data_only: bool) -> float:
        return seq(self.local_transactions) \
            .map(lambda transaction: transaction.get_time(is_save_to_disc, is_useful_data_only)) \
            .sum()

    def memory_usage(self, only_useful_data: bool) -> int:
        return self.replication_factor * seq(self.local_transactions) \
            .map(lambda transaction:
                 transaction.useful_data_amount if only_useful_data else transaction.data_amount) \
            .sum()
