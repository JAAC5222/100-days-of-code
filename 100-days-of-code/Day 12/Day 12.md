# Day 12 - Scope

← [[100-days-of-code/Day 11/Day 11|Day 11]] | [[100-days-of-code/Day 13/Day 13|Day 13]] →

---

## 📝 ¿Qué conceptos aprendí hoy?

[[100-days-of-code/Day 12/Block Scope/task.md|Block Scope]] · [[100-days-of-code/Day 12/Global Constants/task.md|Global Constants]] · [[100-days-of-code/Day 12/Global Vars/task.md|Global Vars]] · [[100-days-of-code/Day 12/Namespaces and Scope/task.md|Namespaces and Scope]] · [[100-days-of-code/Day 12/Number Guessing Project/task.md|Number Guessing Project]]

---

## 💻 Código del día

### main.py

```python
import art
import random

while True:
    print(art.alt_logo)
    print("""Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.""")

    number = random.randint(1, 100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess > number:
            print("Too high! Guess again.")
            lives -= 1
        else:
            print("Too low! Guess again.")
            lives -= 1

    if lives == 0:
        print("You've run out of guesses!")

    if input("Do you want to play again? Type 'y' or 'n': ") == 'y':
        print("\n" * 20)
    else:
        break
```

### art.py

```python
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

alt_logo = r"""
  ________                            .__                  _______               ___.                    ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    \      \  __ __  _____\_ |__   ___________   /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /  \____|__  /____/|__|_|  /___  /\___  >__|     \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/            \/    \/     \/                \/     \/      \/     \/ 
"""
```

### Archivos

[[100-days-of-code/Day 12/Number Guessing Project/main.py|main.py]] · [[100-days-of-code/Day 12/Number Guessing Project/art.py|art.py]]

---

## 🧠 Reflexión

### ¿Qué fue fácil?
- Variables locales vs globales tiene sentido conceptual
- Las constantes globales en MAYÚSCULAS son buena práctica
### ¿Qué fue difícil?
- Entender POR QUÉ no puedo modificar una variable global desde una función sin `global`
- Scope dentro de scope dentro de scope
- Cuándo crear variables globales vs pasarlas como parámetros
### ¿Qué aprendí?
- Las variables locales "mueren" cuando la función termina
- Variables globales pueden causar bugs si no tienes cuidado
- Es mejor pasar variables como parámetros que usar globales

---

## 🏷️ Tags

#scope #variables #functions #exercise #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]

> [!info]- Archivos info de la lección para PyCharm
> [[100-days-of-code/Day 12/lesson-info.yaml|lesson-info]] · [[100-days-of-code/Day 12/lesson-remote-info.yaml|lesson-remote-info]]
