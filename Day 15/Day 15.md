# Day 15 - Coffee Machine

← [[100-days-of-code/Day 14/Day 14|Day 14]] | [[100-days-of-code/Day 16/Day 16|Day 16]] →

---

## 📝 ¿Qué conceptos aprendí hoy?

[[100-days-of-code/Day 15/Coffee Machine Project/task.md|Coffee Machine Project]]

---

## 💻 Código del día

### main.py

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
```

### Archivos

[[100-days-of-code/Day 15/Coffee Machine Project/main.py|main.py]]

---

## 🧠 Reflexión

### ¿Qué fue fácil?
- Diccionarios para recursos (agua, leche, café)
- La lógica de "¿hay suficientes recursos?"
### ¿Qué fue difícil?
- Manejar TODOS los casos: ordenar, reportar recursos, apagar
- Validar que el usuario meta dinero suficiente
- Calcular cambio correctamente
### ¿Qué aprendí?
- Los programas reales tienen muchos "edge cases" (casos especiales)
- While True + break es útil para menús infinitos
- Funciones helper (pequeñas funciones que hacen una cosa) mantienen el código limpio

---

## 🏷️ Tags

#dictionaries #functions #loops #project #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] |  [[MOC - Projects]]

> [!info]- Archivos info de la lección para PyCharm
> [[100-days-of-code/Day 15/lesson-info.yaml|lesson-info]] · [[100-days-of-code/Day 15/lesson-remote-info.yaml|lesson-remote-info]]
