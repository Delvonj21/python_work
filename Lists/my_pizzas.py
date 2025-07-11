pizzas = ["pepperoni", "sausage", "spinach and chicken"]
friend_pizzas = pizzas[:]

pizzas.append("meat love's")
friend_pizzas.append("pesto")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
