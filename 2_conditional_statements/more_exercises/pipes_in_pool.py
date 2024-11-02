volume_of_swimming_pool = int(input())
debit_of_first_pipe = int(input())
debit_of_second_pipe = int(input())
hours_worker_missing = float(input())

water_in_pool = (debit_of_first_pipe + debit_of_second_pipe) * hours_worker_missing

if volume_of_swimming_pool >= water_in_pool:
    print(f"The pool is {(water_in_pool / volume_of_swimming_pool * 100):.2f}% full. "
          f"Pipe 1: {(((debit_of_first_pipe * hours_worker_missing) / water_in_pool) * 100):.2f}%. "
          f"Pipe 2: {(((debit_of_second_pipe * hours_worker_missing) / water_in_pool) * 100):.2f}%.")
else:
    print(f"For {hours_worker_missing} hours the pools "
          f"overflows with {water_in_pool - volume_of_swimming_pool} liters.")


