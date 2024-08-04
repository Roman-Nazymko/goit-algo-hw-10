import pulp

# Створення проблеми лінійного програмування
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішення
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Цільова функція: максимізація кількості вироблених напоїв
prob += lemonade + fruit_juice, "Total_Produced_Drinks"

# Обмеження на ресурси
prob += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
prob += 1 * lemonade <= 50, "Sugar"
prob += 1 * lemonade <= 30, "LemonJuice"
prob += 2 * fruit_juice <= 40, "FruitPuree"

# Розв'язання задачі
prob.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Produced Lemonade: {pulp.value(lemonade)}")
print(f"Produced Fruit Juice: {pulp.value(fruit_juice)}")
print(f"Total Produced Drinks: {pulp.value(prob.objective)}")
