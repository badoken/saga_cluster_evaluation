from dataclasses import dataclass
import random


@dataclass
class Transaction:
    transaction_time = random.uniform(100, 500)  # ms
    data_amount = random.randint(1000, 3000)  # Bytes
    _useful_data_coef = random.uniform(0.1, 1)
    useful_data_amount = int(data_amount * _useful_data_coef)
    _memory_throughput = 10 ** 6  # 1 MByte/ms
    _network_throughput = 125 * 10 ** 3  # 1 KByte/ms

    def _get_transfer_time(self, only_useful_data: bool) -> float:
        return self.required_memory(only_useful_data) / self._network_throughput

    def _get_persist_time(self, only_useful_data: bool) -> float:
        return self.required_memory(only_useful_data) / self._memory_throughput

    def get_time(self, is_save_to_disc: bool, is_useful_data_only: bool) -> float:
        return self.transaction_time + \
               self._get_transfer_time(only_useful_data=is_useful_data_only) + \
               (self._get_persist_time(only_useful_data=is_useful_data_only) if is_save_to_disc else 0)

    def required_memory(self, only_useful_data: bool):
        return self.useful_data_amount if only_useful_data else self.data_amount
