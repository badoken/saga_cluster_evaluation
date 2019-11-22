from matplotlib import pyplot

from transaction import Transaction

transactions = [Transaction() for n in range(0, 20)]

print("Transactions are:\n" + str(transactions))

# t_repl = lambda transaction_id, use_persistence: t_transac(transaction_id) + if (use_persistence)

sum_time_of_all_data_and_save_to_disc = \
    list(map(lambda transaction: transaction.get_sum_time(True, False), transactions))
sum_time_of_all_data_and_dont_save_to_disc = \
    list(map(lambda transaction: transaction.get_sum_time(False, False), transactions))
sum_time_of_useful_data_and_save_to_disc = \
    list(map(lambda transaction: transaction.get_sum_time(True, True), transactions))
sum_time_of_useful_data_and_dont_save_to_disc = \
    list(map(lambda transaction: transaction.get_sum_time(False, True), transactions))

pyplot.plot(sum_time_of_all_data_and_save_to_disc)
pyplot.plot(sum_time_of_all_data_and_dont_save_to_disc)
pyplot.plot(sum_time_of_useful_data_and_save_to_disc)
pyplot.plot(sum_time_of_useful_data_and_dont_save_to_disc)
pyplot.legend(['all data with save to disc',
               'all data without save to disc',
               'useful data with save to disc',
               'useful data without save to disc'],
              loc='upper left')
pyplot.title("One distributed transaction")
pyplot.xlabel("time")
pyplot.ylabel("local transaction number")
pyplot.show()
