import random

from functional import seq

from distributed_transaction import SaveType
from distributed_transaction_factory import DistributedTransactionFactory
from memory_evaluation import MemoryEvaluation
from time_evaluation import TimeEvaluation

replication_factor = 3
distributed_transactions_count = 5000

distributed_transaction_factory = DistributedTransactionFactory(replication_factor)

distribute_transactions = [distributed_transaction_factory.generate(random.randint(7, 20))
                           for n in range(distributed_transactions_count)]

time_evaluation = TimeEvaluation(distribute_transactions)
memory_evaluation = MemoryEvaluation(distribute_transactions)

print("___Time optimizations___")
print("No save, no data optimization: " + str(time_evaluation.time_optimization(save_type=SaveType.NONE,
                                                                                is_useful_data_only=False)))
print("No save, with data optimization: " + str(time_evaluation.time_optimization(save_type=SaveType.NONE,
                                                                                  is_useful_data_only=True)))

print("Failures save, no data optimization: " + str(time_evaluation.time_optimization(save_type=SaveType.FAILURES,
                                                                                      is_useful_data_only=False)))
print("Failures save, with data optimization: " + str(time_evaluation.time_optimization(save_type=SaveType.FAILURES,
                                                                                        is_useful_data_only=True)))

print("All save, with data optimization: " + str(time_evaluation.time_optimization(save_type=SaveType.ALL,
                                                                                   is_useful_data_only=True)))
print("All save, no data optimization: " + str(time_evaluation.time_optimization(save_type=SaveType.ALL,
                                                                                 is_useful_data_only=False)))

print("\n___Memory optimizations___")
for r in range(2, 6):
    print("Replication factor: " + str(r))
    save_no_opt = memory_evaluation.optimization_and_memory(save_type=SaveType.ALL, only_useful_data=False, replicas=r)
    print("All save, no data optimization: " + str(save_no_opt[1]) + ", opt = " + str(save_no_opt[0]))
    save_opt = memory_evaluation.optimization_and_memory(save_type=SaveType.ALL, only_useful_data=True, replicas=r)
    print("All save, with data optimization: " + str(save_opt[1]) + ", opt = " + str(save_opt[0]))
    failures_no_opt = memory_evaluation.optimization_and_memory(save_type=SaveType.FAILURES, only_useful_data=False,
                                                                replicas=r)
    print("Failures save, no data optimization: " + str(failures_no_opt[1]) + ", opt = " + str(failures_no_opt[0]))
    failures_opt = memory_evaluation.optimization_and_memory(save_type=SaveType.FAILURES, only_useful_data=True,
                                                             replicas=r)
    print("Failures save, with data optimization: " + str(failures_opt[1]) + ", opt = " + str(failures_opt[0]))
