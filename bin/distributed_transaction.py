from dataclasses import dataclass
from transaction import Transaction
from functional import seq


@dataclass
class DistributedTransaction:
    local_transactions: [Transaction]

    def summary_transaction_time(self, is_save_to_disc: bool, is_useful_data_only: bool) -> float:
        return seq(self.local_transactions) \
            .map(lambda transaction: transaction.get_time(is_save_to_disc, is_useful_data_only)) \
            .sum()
