# Day 10 - Calculator

← [[100-days-of-code/Day 9/Day 9|Day 9]] | [[100-days-of-code/Day 11/Day 11|Day 11]] →

---

## 📝 ¿Qué conceptos aprendí hoy?

[[100-days-of-code/Day 10/Calculator Project/task.md|Calculator Project]] · [[100-days-of-code/Day 10/Docstrings/task.md|Docstrings]] · [[100-days-of-code/Day 10/Functions with Outputs/task.md|Functions with Outputs]] · [[100-days-of-code/Day 10/Multiple Return Values/task.md|Multiple Return Values]]

---

## 💻 Código del día

### main.py

```python
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    print(art.logo)
    result = 0
    num1 = int(input("What's the first number?: "))
    valid_operation = False
    finish = False
    while not finish:
        while not valid_operation:
            print("+\n-\n*\n/")
            operation = input("Pick an operation: ")
            if operation in operations:
                valid_operation = True
                num2 = int(input("What's the second number?: "))
                result = operations[operation](num1, num2)
                print(f"{num1} {operation} {num2} = {result}")
            else:
                print("Invalid operation, please type a valid operation")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            valid_operation = False
            num1 = result
        else:
            finish = True
            print("\n" * 20)
```

### art.py

```python
logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
```

### Archivos

[[100-days-of-code/Day 10/Calculator Project/main.py|main.py]] · [[100-days-of-code/Day 10/Calculator Project/art.py|art.py]]

---

## 🧠 Reflexión

### ¿Qué fue fácil?
- Funciones con `return` tienen sentido: procesan algo y lo devuelven
- Combinar funciones en un programa más grande
### ¿Qué fue difícil?
- Entender qué es lo que devuelve `return` vs solo hacer `print()`
- Docstrings parecen comentarios pero son diferentes
- La recursión (llamar a la función desde sí misma)
### ¿Qué aprendí?
- `return` es como "la respuesta" que da la función
- Los docstrings documentan qué hace la función
- Sin `return`, la función devuelve `None`

---

## 🏷️ Tags

#functions #return #docstrings #project #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]

> [!info]- Archivos info de la lección para PyCharm
> [[100-days-of-code/Day 10/lesson-info.yaml|lesson-info]] · [[100-days-of-code/Day 10/lesson-remote-info.yaml|lesson-remote-info]]
