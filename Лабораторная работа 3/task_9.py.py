salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение


while months != 0:
    delta = spend - salary

    months -= 1
    money_capital += delta
    spend *= 1 + increase

print(round(money_capital))
