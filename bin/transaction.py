from dataclasses import dataclass
import random


@dataclass
class Transaction:
    transaction_time: float
    data_amount: int
    useful_data_coef: float
    useful_data_amount: int

    def __init__(self):
        self.transaction_time = random.uniform(100, 500)
        self.data_amount = random.randint(3, 10)
        self.useful_data_coef = random.random()
        self.useful_data_amount = int(self.data_amount * self.useful_data_coef)

    def _get_transfer_time(self, only_useful_data: bool) -> float:
        return 10 + (self.useful_data_amount if only_useful_data else self.data_amount) * 2

    def _get_persist_time(self, only_useful_data: bool) -> float:
        return 40 + (self.useful_data_amount if only_useful_data else self.data_amount) * 5

    def get_time(self, is_save_to_disc: bool, is_useful_data_only: bool) -> float:
        return self.transaction_time + \
               self._get_transfer_time(only_useful_data=is_useful_data_only) + \
               (self._get_persist_time(only_useful_data=is_useful_data_only) if is_save_to_disc else 0)
