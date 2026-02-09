# Day 3 - Control Flow

← [[100-days-of-code/Day 2/Day 2|Day 2]] | [[100-days-of-code/Day 4/Day 4|Day 4]] →

---

## 📝 ¿Qué conceptos aprendí hoy?

[[100-days-of-code/Day 3/If Else/task.md|If Else]] · [[100-days-of-code/Day 3/Logical Operators/task.md|Logical Operators]] · [[100-days-of-code/Day 3/Modulo/task.md|Modulo]] · [[100-days-of-code/Day 3/Multiple Ifs/task.md|Multiple Ifs]] · [[100-days-of-code/Day 3/Nesting and Elif/task.md|Nesting and Elif]] · [[100-days-of-code/Day 3/Python Pizza/task.md|Python Pizza]] · [[100-days-of-code/Day 3/Treasure Island Project/task.md|Treasure Island Project]]

---

## 💻 Código del día

### main.py

```python
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell in to a hole. Game Over.")
```

### Archivos

[[100-days-of-code/Day 3/Treasure Island Project/main.py|main.py]]

---

## 🧠 Reflexión

### ¿Qué fue fácil?

- If/else tiene sentido lógico: "si pasa X, haz Y"
- Los operadores de comparación (>, <, \==) son intuitivos
### ¿Qué aprendí?

- Python usa indentación en lugar de llaves `{}`
- `elif` es mejor que múltiples `if` cuando solo una condición debe ejecutarse
- El operador `%` (modulo) es perfecto para saber si algo es par/impar

---

## 🏷️ Tags

#control-flow #conditionals #operators #exercise #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]

> [!info]- Archivos info de la lección para PyCharm
> [[100-days-of-code/Day 3/lesson-info.yaml|lesson-info]] · [[100-days-of-code/Day 3/lesson-remote-info.yaml|lesson-remote-info]]
