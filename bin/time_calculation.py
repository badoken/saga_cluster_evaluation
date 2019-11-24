import random

from functional import seq
from matplotlib import pyplot

from distributed_transaction_factory import DistributedTransactionFactory

replication_factor = 3

distributed_transaction_factory = DistributedTransactionFactory(replication_factor)

distribute_transactions = [distributed_transaction_factory.generate(random.randint(7, 20)) for n in range(0, 2_000)]

first_distributed_transaction = distribute_transactions[0]

local_transaction_times = {
    'all data with save to disc': list(map(
        lambda transaction: transaction.get_time(is_save_to_disc=True, is_useful_data_only=False),
        first_distributed_transaction.local_transactions)),
    'useful data with save to disc': list(map(
        lambda transaction: transaction.get_time(is_save_to_disc=True, is_useful_data_only=True),
        first_distributed_transaction.local_transactions)),
    'all data without save to disc': list(map(
        lambda transaction: transaction.get_time(is_save_to_disc=False, is_useful_data_only=False),
        first_distributed_transaction.local_transactions)),
    'useful data without save to disc': list(map(
        lambda transaction: transaction.get_time(is_save_to_disc=False, is_useful_data_only=True),
        first_distributed_transaction.local_transactions))
}

figure1 = pyplot.figure(1)
pyplot.title("Local transactions time of one distributed transaction")
for transaction_time in local_transaction_times.values():
    pyplot.plot(transaction_time)
pyplot.legend(local_transaction_times.keys(), loc='upper left')
pyplot.xlabel("local transaction number")
pyplot.ylabel("time")

distributed_transaction_times_if_all_data_and_save_to_disc = list(map(
    lambda d_transaction: d_transaction.summary_transaction_time(is_save_to_disc=True, is_useful_data_only=False),
    distribute_transactions))
distributed_transaction_times_if_useful_data_and_save_to_disc = list(map(
    lambda d_transaction: d_transaction.summary_transaction_time(is_save_to_disc=True, is_useful_data_only=True),
    distribute_transactions))
distributed_transaction_times_if_all_data_and_no_save_to_disc = list(map(
    lambda d_transaction: d_transaction.summary_transaction_time(is_save_to_disc=False, is_useful_data_only=False),
    distribute_transactions))
distributed_transaction_times_if_useful_data_and_no_save_to_disc = list(map(
    lambda d_transaction: d_transaction.summary_transaction_time(is_save_to_disc=False, is_useful_data_only=True),
    distribute_transactions))

figure2 = pyplot.figure(2)
pyplot.title("Distributed transactions time")
pyplot.plot(distributed_transaction_times_if_all_data_and_save_to_disc)
pyplot.plot(distributed_transaction_times_if_useful_data_and_save_to_disc)
pyplot.plot(distributed_transaction_times_if_all_data_and_no_save_to_disc)
pyplot.plot(distributed_transaction_times_if_useful_data_and_no_save_to_disc)
pyplot.legend(['all data with save to disc',
               'useful data with save to disc',
               'all data without save to disc',
               'useful data without save to disc'],
              loc='upper left')
pyplot.xlabel("distributed transaction number")
pyplot.ylabel("time")

distributed_transactions_sum_time = {
    'all data with save to disc': seq(distributed_transaction_times_if_all_data_and_save_to_disc).sum(),
    'useful data with save to disc': seq(distributed_transaction_times_if_useful_data_and_save_to_disc).sum(),
    'all data without save to disc': seq(distributed_transaction_times_if_all_data_and_no_save_to_disc).sum(),
    'useful data without save to disc': seq(distributed_transaction_times_if_useful_data_and_no_save_to_disc).sum()
}

figure3 = pyplot.figure(3)
pyplot.title("Summary time required for " + str(len(distribute_transactions)) + " distributed transactions")
pyplot.bar(x=distributed_transactions_sum_time.keys(), height=distributed_transactions_sum_time.values())
print("Symmary time for distributed transactions: " + str(distributed_transactions_sum_time))

distributed_transactions_sum_memory = {
    'all data': seq(distribute_transactions).map(lambda d_t: d_t.memory_usage(only_useful_data=False)).sum(),
    'useful data': seq(distribute_transactions).map(lambda d_t: d_t.memory_usage(only_useful_data=True)).sum()
}

figure4 = pyplot.figure(4)
pyplot.title("Memory requirements for " + str(len(distribute_transactions)) + " distributed transactions with " +
             str(replication_factor) + " replication factor")
pyplot.bar(x=distributed_transactions_sum_memory.keys(), height=distributed_transactions_sum_memory.values())

pyplot.show()
