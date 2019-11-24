import random

from functional import seq
from matplotlib import pyplot

from distributed_transaction_factory import DistributedTransactionFactory
from transaction import Transaction

distributed_transaction_factory = DistributedTransactionFactory()

distribute_transactions = [distributed_transaction_factory.generate(random.randint(7, 20)) for n in range(0, 2_000)]

first_distributed_transaction = distribute_transactions[0]

local_transaction_times_if_all_data_and_save_to_disc = list(map(
    lambda transaction: transaction.get_time(is_save_to_disc=True, is_useful_data_only=False),
    first_distributed_transaction.local_transactions))
local_transaction_times_if_all_data_and_no_save_to_disc = list(map(
    lambda transaction: transaction.get_time(is_save_to_disc=False, is_useful_data_only=False),
    first_distributed_transaction.local_transactions))
local_transaction_times_if_useful_data_and_save_to_disc = list(map(
    lambda transaction: transaction.get_time(is_save_to_disc=True, is_useful_data_only=True),
    first_distributed_transaction.local_transactions))
local_transactions_time_if_useful_data_and_no_save_to_disc = list(map(
    lambda transaction: transaction.get_time(is_save_to_disc=False, is_useful_data_only=True),
    first_distributed_transaction.local_transactions))

figure1 = pyplot.figure(1)
pyplot.title("Local transactions time of one distributed transaction")
pyplot.plot(local_transaction_times_if_all_data_and_save_to_disc)
pyplot.plot(local_transaction_times_if_all_data_and_no_save_to_disc)
pyplot.plot(local_transaction_times_if_useful_data_and_save_to_disc)
pyplot.plot(local_transactions_time_if_useful_data_and_no_save_to_disc)
pyplot.legend(['all data with save to disc',
               'all data without save to disc',
               'useful data with save to disc',
               'useful data without save to disc'],
              loc='upper left')
pyplot.xlabel("local transaction number")
pyplot.ylabel("time")

distributed_transaction_times_if_all_data_and_save_to_disc = list(map(
    lambda d_transaction: d_transaction.summary_transaction_time(is_save_to_disc=True, is_useful_data_only=False),
    distribute_transactions))
distributed_transaction_times_if_all_data_and_no_save_to_disc = list(map(
    lambda d_transaction: d_transaction.summary_transaction_time(is_save_to_disc=False, is_useful_data_only=False),
    distribute_transactions))
distributed_transaction_times_if_useful_data_and_save_to_disc = list(map(
    lambda d_transaction: d_transaction.summary_transaction_time(is_save_to_disc=True, is_useful_data_only=True),
    distribute_transactions))
distributed_transaction_times_if_useful_data_and_no_save_to_disc = list(map(
    lambda d_transaction: d_transaction.summary_transaction_time(is_save_to_disc=False, is_useful_data_only=True),
    distribute_transactions))

figure2 = pyplot.figure(2)
pyplot.title("Distributed transactions time")
pyplot.plot(distributed_transaction_times_if_all_data_and_save_to_disc)
pyplot.plot(distributed_transaction_times_if_all_data_and_no_save_to_disc)
pyplot.plot(distributed_transaction_times_if_useful_data_and_save_to_disc)
pyplot.plot(distributed_transaction_times_if_useful_data_and_no_save_to_disc)
pyplot.legend(['all data with save to disc',
               'all data without save to disc',
               'useful data with save to disc',
               'useful data without save to disc'],
              loc='upper left')
pyplot.xlabel("distributed transaction number")
pyplot.ylabel("time")

distributed_transactions_summary_time_if_all_data_and_save_to_disc = \
    seq(distributed_transaction_times_if_all_data_and_save_to_disc).sum()
distributed_transactions_summary_time_if_all_data_and_no_save_to_disc = seq(
    distributed_transaction_times_if_all_data_and_no_save_to_disc).sum()
distributed_transactions_summary_time_if_useful_data_and_save_to_disc = \
    seq(distributed_transaction_times_if_useful_data_and_save_to_disc).sum()
distributed_transactions_summary_time_if_useful_data_and_no_save_to_disc = \
    seq(distributed_transaction_times_if_useful_data_and_no_save_to_disc).sum()

figure3 = pyplot.figure(3)
pyplot.title("Summary time required for " + str(len(distribute_transactions)) + "distributed transactions")
print("summary times: " + str([distributed_transactions_summary_time_if_all_data_and_save_to_disc,
                               distributed_transactions_summary_time_if_all_data_and_no_save_to_disc,
                               distributed_transactions_summary_time_if_useful_data_and_save_to_disc,
                               distributed_transactions_summary_time_if_useful_data_and_no_save_to_disc]))
pyplot.hist([distributed_transactions_summary_time_if_all_data_and_save_to_disc,
             distributed_transactions_summary_time_if_all_data_and_no_save_to_disc,
             distributed_transactions_summary_time_if_useful_data_and_save_to_disc,
             distributed_transactions_summary_time_if_useful_data_and_no_save_to_disc])
# pyplot.legend(['all data with save to disc',
#                'all data without save to disc',
#                'useful data with save to disc',
#                'useful data without save to disc'],
#               loc='upper left')
# pyplot.xlabel("distributed transaction number")
# pyplot.ylabel("time")

pyplot.show()
