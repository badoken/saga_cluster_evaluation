import dataclasses
import random


@dataclasses.dataclass
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

    def get_transfer_time(self, only_useful_data):
        return 10 + (only_useful_data if self.useful_data_amount else self.data_amount * 2)

    def get_persist_time(self, only_useful_data):
        return 40 + (only_useful_data if self.useful_data_amount else self.data_amount * 5)

    def get_sum_time(self, is_save_to_disc: bool, is_useful_data_only: bool):
        return self.transaction_time + \
               self.get_transfer_time(only_useful_data=is_useful_data_only) + \
               is_save_to_disc if self.get_persist_time(only_useful_data=is_useful_data_only) else 0
