import random
from dataclasses import dataclass
from enum import Enum

from functional import seq

from transaction import Transaction


class SaveType(Enum):
    NONE = 0,
    FAILURES = 1,
    ALL = 2


@dataclass
class DistributedTransaction:
    local_transactions: [Transaction]
    replication_factor: int = 3
    failure_probability: int = 5

    def __post_init__(self) -> None:
        self._is_failed: bool = random.randint(1, 100) <= self.failure_probability
        self._failed_num: int = random.randint(0, len(self.local_transactions)) if self._is_failed else -1

    def summary_transaction_time(self, save_type: SaveType, is_useful_data_only: bool) -> float:
        if self._is_failed:
            return seq(self.local_transactions) \
                .take(self._failed_num) \
                .zip_with_index() \
                .map(lambda t_i:
                     (2 if t_i[1] < self._failed_num else 1) * t_i[0].get_time(
                         is_save_to_disc=(save_type != SaveType.NONE),
                         is_useful_data_only=is_useful_data_only)
                     ) \
                .sum()
        else:
            return seq(self.local_transactions) \
                .map(lambda t:
                     t.get_time(is_save_to_disc=(save_type == SaveType.ALL),
                                is_useful_data_only=is_useful_data_only)) \
                .sum()

    def memory_usage(self, save_type: SaveType, only_useful_data: bool) -> int:
        if self._is_failed:
            return self.replication_factor * seq(self.local_transactions) \
                .take(self._failed_num) \
                .filter(lambda t: save_type != SaveType.NONE) \
                .zip_with_index() \
                .map(lambda t:
                     (2 if t[1] < self._failed_num else 1) * t[0].required_memory(only_useful_data)) \
                .sum()
        else:
            return self.replication_factor * seq(self.local_transactions) \
                .filter(lambda t: save_type == SaveType.ALL) \
                .map(lambda t: t.required_memory(only_useful_data)) \
                .sum()
