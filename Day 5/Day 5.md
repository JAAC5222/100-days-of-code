# Day 5 - For Loops

← [[100-days-of-code/Day 4/Day 4|Day 4]] | [[100-days-of-code/Day 6/Day 6|Day 6]] →

---

## 📝 ¿Qué conceptos aprendí hoy?

[[100-days-of-code/Day 5/For Loops/task.md|For Loops]] · [[100-days-of-code/Day 5/For Loops with Range/task.md|For Loops with Range]] · [[100-days-of-code/Day 5/Highest Score/task.md|Highest Score]] · [[100-days-of-code/Day 5/Password Generator Project/task.md|Password Generator Project]]

---

## 💻 Código del día

### main.py

```python
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
```

### Archivos

[[100-days-of-code/Day 5/Password Generator Project/main.py|main.py]]

---

## 🧠 Reflexión

### ¿Qué fue fácil?

- El concepto de "repetir algo varias veces" es claro
- Iterar sobre una lista es más simple de lo que parece
### Observaciones

- For loops son MUCHO más eficientes que copiar/pegar código 20 veces
- `range(start, stop, step)` es MUY flexible
- Puedes hacer loops dentro de loops

---

## 🏷️ Tags

#loops #for-loop #range #exercise #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]

> [!info]- Archivos info de la lección para PyCharm
> [[100-days-of-code/Day 5/lesson-info.yaml|lesson-info]] · [[100-days-of-code/Day 5/lesson-remote-info.yaml|lesson-remote-info]]
