# Day 4 - Lists & Randomisation

← [[100-days-of-code/Day 3/Day 3|Day 3]] | [[100-days-of-code/Day 5/Day 5|Day 5]] →

---

## 📝 ¿Qué conceptos aprendí hoy?

[[100-days-of-code/Day 4/Banker Roulette/task.md|Banker Roulette]] · [[100-days-of-code/Day 4/IndexError/task.md|IndexError]] · [[100-days-of-code/Day 4/Lists/task.md|Lists]] · [[100-days-of-code/Day 4/Random Module/task.md|Random Module]] · [[100-days-of-code/Day 4/Rock Paper Scissors/task.md|Rock Paper Scissors]]

---

## 💻 Código del día

### main.py

```python
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
```

### Archivos

[[100-days-of-code/Day 4/Rock Paper Scissors/main.py|main.py]]

---

## 🧠 Reflexión

### ¿Qué fue fácil?

- Las listas son como cajones con compartimentos numerados
- Acceder a elementos con `[0], [1], [2]` tiene sentido
### Observaciones

- `len(lista)` te da el tamaño
- `random.choice()` es perfecto para elegir elementos aleatorios
- Las listas pueden contener diferentes tipos de datos

---

## 🏷️ Tags

#lists #indexing #modules #exercise #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]

> [!info]- Archivos info de la lección para PyCharm
> [[100-days-of-code/Day 4/lesson-info.yaml|lesson-info]] · [[100-days-of-code/Day 4/lesson-remote-info.yaml|lesson-remote-info]]
