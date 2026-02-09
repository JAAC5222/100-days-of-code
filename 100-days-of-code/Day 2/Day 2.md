# Day 2 - Data Types & Operations

← [[100-days-of-code/Day 1/Day 1|Day 1]] | [[100-days-of-code/Day 3/Day 3|Day 3]] →

---

## 📝 ¿Qué conceptos aprendí hoy?

[[100-days-of-code/Day 2/Data Types/task.md|Data Types]] · [[100-days-of-code/Day 2/Mathematical Operations/task.md|Mathematical Operations]] · [[100-days-of-code/Day 2/Number Manipulation/task.md|Number Manipulation]] · [[100-days-of-code/Day 2/Tip Calculator Project/task.md|Tip Calculator Project]] · [[100-days-of-code/Day 2/Type Error, Checking and Conversion/task.md|Type Error, Checking and Conversion]]

---

## 💻 Código del día

### main.py

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
```

### Archivos

[[100-days-of-code/Day 2/Tip Calculator Project/main.py|main.py]]

---

## 🧠 Reflexión

### ¿Qué fue fácil?

- Operaciones matemáticas básicas (+, -,\*, /)
- El concepto de diferentes tipos de datos tiene sentido
### Observaciones

- Type casting es básicamente "convertir de un tipo a otro"

---

## 🏷️ Tags

#variables #operators #data-types #exercise #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]

> [!info]- Archivos info de la lección para PyCharm
> [[100-days-of-code/Day 2/lesson-info.yaml|lesson-info]] · [[100-days-of-code/Day 2/lesson-remote-info.yaml|lesson-remote-info]]
