from dataclasses import dataclass, replace
from typing import Tuple

from functional import seq

from distributed_transaction import SaveType, DistributedTransaction


@dataclass
class MemoryEvaluation:
    transactions: [DistributedTransaction]

    def all_transactions_memory(self, only_useful_data: bool, save_type: SaveType, replicas: int) -> int:
        return seq(self.transactions) \
            .map(lambda d_t: replace(d_t, replication_factor=replicas)) \
            .map(lambda updated_d_t: updated_d_t.memory_usage(save_type, only_useful_data)) \
            .sum()

    def optimization_and_memory(self, only_useful_data: bool, save_type: SaveType, replicas: int) \
            -> Tuple[float, float]:
        required_memory = self.all_transactions_memory(only_useful_data, save_type, replicas)
        return \
            100 - (required_memory * 100 / self.all_transactions_memory(False, SaveType.ALL, replicas)), \
            required_memory
