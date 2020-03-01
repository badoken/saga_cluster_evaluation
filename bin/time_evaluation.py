from dataclasses import dataclass

from functional import seq

from distributed_transaction import SaveType, DistributedTransaction
from transaction import Transaction


@dataclass
class TimeEvaluation:
    transactions: [DistributedTransaction]

    def all_transactions_time(self, save_type: SaveType, is_useful_data_only: bool) -> float:
        return seq(self.transactions) \
            .map(lambda d_t: d_t.summary_transaction_time(save_type=save_type,
                                                          is_useful_data_only=is_useful_data_only)) \
            .sum()

    def time_optimization(self, save_type: SaveType, is_useful_data_only: bool) -> float:
        return 100 - (self.all_transactions_time(save_type, is_useful_data_only) *
                      100 / self.all_transactions_time_default)

    def __post_init__(self):
        self.all_transactions_time_default: float = self.all_transactions_time(save_type=SaveType.ALL,
                                                                               is_useful_data_only=False)
