# Day 9 - Blind Auction

← [[100-days-of-code/Day 8/Day 8|Day 8]] | [[100-days-of-code/Day 10/Day 10|Day 10]] →

---

## 📝 ¿Qué conceptos aprendí hoy?

[[100-days-of-code/Day 9/Blind Auction Project/task.md|Blind Auction Project]] · [[100-days-of-code/Day 9/Dictionaries/task.md|Dictionaries]] · [[100-days-of-code/Day 9/Nested Lists and Dictionaries/task.md|Nested Lists and Dictionaries]]

---

## 💻 Código del día

### main.py

```python
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

auction = {}

print(art.logo)

maxBid = 0

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    auction[name] = bid
    if bid > maxBid:
        maxBid = bid

    keep = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if keep == "yes":
        continue
    elif keep == "no":
        winner = [k for k, v in auction.items() if v == maxBid]
        if len(winner) == 1:
            print("The winner is ", winner[0], "with a bid of ", maxBid, ".")
        elif len(winner) > 1:
            print(f"The winners are ", end='')
            for i in winner:
                print(i, end=" ")
            print(f"with a bid of {maxBid}.")
    break
```

### art.py

```python
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
```

### Archivos

[[100-days-of-code/Day 9/Blind Auction Project/main.py|main.py]] · [[100-days-of-code/Day 9/Blind Auction Project/art.py|art.py]]

---

## 🧠 Reflexión

### ¿Qué fue fácil?
- Los diccionarios son como listas pero con "etiquetas" en lugar de números
- Key-value pairs tienen mucho sentido: nombre → valor
### ¿Qué fue difícil?
- Sintaxis de diccionarios: `{}` vs `[]
- Iterar sobre diccionarios con `.items()`, `.keys()`, `.values()`
### ¿Qué aprendí?
- Los diccionarios son perfectos para datos estructurados
- Puedes tener listas dentro de diccionarios y viceversa
- `clear()` para limpiar la consola hace el programa más dinámico

---

## 🏷️ Tags

#dictionaries #structures #project #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]

> [!info]- Archivos info de la lección para PyCharm
> [[100-days-of-code/Day 9/lesson-info.yaml|lesson-info]] · [[100-days-of-code/Day 9/lesson-remote-info.yaml|lesson-remote-info]]
