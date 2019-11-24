from dataclasses import dataclass

from distributed_transaction import DistributedTransaction
from transaction import Transaction


@dataclass
class DistributedTransactionFactory:
    replication_factor: int = 1

    def generate(self, count: int) -> DistributedTransaction:
        if count <= 0:
            raise ValueError("Count should be possible")
        return DistributedTransaction(local_transactions=[Transaction() for i in range(0, count)],
                                      replication_factor=self.replication_factor)
