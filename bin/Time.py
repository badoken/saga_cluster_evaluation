from matplotlib import pyplot

from Transaction import Transaction

transactions1 = [Transaction() for n in range(0, 20)]

print("Transactions are:\n" + str(transactions1))


def distributed_transaction_time(transactions: [Transaction],
                                 is_save_to_disc: bool,
                                 is_useful_data_only: bool):
    # return [
    #
    #     for (transaction_1, transaction_2) in zip(transactions[: -1], transactions[1:])
    # ]

    # t_repl = lambda transaction_id, use_persistence: t_transac(transaction_id) + if (use_persistence)

    x = [1, 2, 3]
    y = [1, 9, 4]

    pyplot.plot(x, y, '--')
    pyplot.title("Test plot")
    pyplot.xlabel("x")
    pyplot.ylabel("y")
    pyplot.show()
