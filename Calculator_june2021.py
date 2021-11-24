print('Сколько денег надо накопить?\n')
deposit_goal = int(input())
print('Сколько уже есть?\n')
deposit_base = int(input())
deposit_delta = int(deposit_goal - deposit_base)
print('До целевого значения осталось ' + str(int(deposit_delta)))

