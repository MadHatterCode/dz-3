ask_num = int(input("Please, type in a 5-digit number to reverse: "))

first_pair, second_pair = divmod(ask_num, 1000)
first_num, second_num = divmod(first_pair, 10)
third_num = second_pair // 100
fourth_num, fifth_num = divmod(second_pair - (third_num * 100), 10)

print((fifth_num * 10000) + (fourth_num * 1000) + (third_num * 100) + (second_num * 10) + first_num)
