#лгов:",round((pillow),2))
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
expense_sum = 0
pillow = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

for i in range (1, months+1):
    pillow += spend - salary
    # months -= 1
    spend *= 1 + increase
    #print(pillow,i)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",round((pillow),2))