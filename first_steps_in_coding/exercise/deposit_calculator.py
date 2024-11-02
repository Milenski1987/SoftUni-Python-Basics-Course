deposited_amount = float(input())
term_of_deposit = int(input())
yearly_rate = float(input())
yearly_rate_in_percent = yearly_rate / 100

final_sum = deposited_amount + term_of_deposit * ((deposited_amount * yearly_rate_in_percent) / 12)

print(final_sum)
