from dataclasses import dataclass
from transaction import Transaction
from functional import seq


@dataclass
class DistributedTransaction:
    local_transactions: [Transaction]
    replication_factor: int = 1

    def summary_transaction_time(self, is_save_to_disc: bool, is_useful_data_only: bool) -> float:
        return seq(self.local_transactions) \
            .map(lambda t: t.get_time(is_save_to_disc, is_useful_data_only)) \
            .sum()

    def memory_usage(self, only_useful_data: bool) -> int:
        return self.replication_factor * seq(self.local_transactions) \
            .map(lambda t: t.useful_data_amount if only_useful_data else t.data_amount) \
            .sum()
