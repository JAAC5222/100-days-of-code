# Day 8 - Caesar Cipher

← [[100-days-of-code/Day 7/Day 7|Day 7]] | [[100-days-of-code/Day 9/Day 9|Day 9]] →

---

## 📝 ¿Qué conceptos aprendí hoy?

[[100-days-of-code/Day 8/Caesar Cipher 1/task.md|Caesar Cipher 1]] · [[100-days-of-code/Day 8/Caesar Cipher 2/task.md|Caesar Cipher 2]] · [[100-days-of-code/Day 8/Caesar Cipher 3/task.md|Caesar Cipher 3]] · [[100-days-of-code/Day 8/Functions with Inputs/task.md|Functions with Inputs]] · [[100-days-of-code/Day 8/Positional vs Keyword Arguments/task.md|Positional vs Keyword Arguments]]

---

## 💻 Código del día

### main.py

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


encrypt(original_text=text, shift_amount=shift)
```

### Archivos

[[100-days-of-code/Day 8/Caesar Cipher 1/main.py|main.py]]

---

## 🧠 Reflexión

### ¿Qué fue fácil?
- Ya entiendo funciones, así que definir `encrypt()` y `decrypt()` fue claro
- El concepto de desplazar letras en el alfabeto
### ¿Qué fue difícil?
- Hacer que funcione con el abecedario circular (después de 'z' vuelve a 'a')
### ¿Qué aprendí?
- Los parámetros hacen las funciones flexibles
- Puedes tener múltiples parámetros: `def encrypt(text, shift, direction)`
- Las funciones pueden llamar a otras funciones

---

## 🏷️ Tags

#functions #parameters #strings #project #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]

> [!info]- Archivos info de la lección para PyCharm
> [[100-days-of-code/Day 8/lesson-info.yaml|lesson-info]] · [[100-days-of-code/Day 8/lesson-remote-info.yaml|lesson-remote-info]]
