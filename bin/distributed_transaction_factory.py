from distributed_transaction import DistributedTransaction
from transaction import Transaction


class DistributedTransactionFactory:
    def generate(self, count: int) -> DistributedTransaction:
        if count <= 0:
            raise ValueError("Count should be possible")
        return DistributedTransaction([Transaction() for i in range(0, count)])
