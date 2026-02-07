# Day 8 - Caesar Cipher

← [[100-days-of-code/Day 7/Day 7|Day 7]] | [[100-days-of-code/Day 9/Day 9|Day 9]] →

---
## 📝 ¿Qué conceptos aprendí hoy?
Funciones con parámetros, cipher, ASCII

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 6/Day 6|Day 6]] - Funciones con parámetros
- [[100-days-of-code/Day 5/Day 5|Day 5]] - Loops para recorrer el alfabeto
- [[100-days-of-code/Day 4/Day 4|Day 4]] - Listas para el alfabeto
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Control flow para direcciones (encrypt/decrypt)
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Strings para el texto a encriptar

---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 8/Caesar Cipher 1";
const folder = app.vault.getAbstractFileByPath(dayFolder);

if (folder && folder.children) {
    const mainFile = folder.children.find(f => f.basename === 'main' && f.extension === 'py');
    
    if (mainFile) {
        const content = await app.vault.read(mainFile);
        dv.header(3, 'Caesar Cipher 1/main.py');
        dv.paragraph("```python\n" + content + "\n```");
    } else {
        dv.paragraph("*No se encontró main.py en esta carpeta*");
    }
}
```
```dataviewjs
const dayFolder = "100-days-of-code/Day 8/Caesar Cipher 2";
const folder = app.vault.getAbstractFileByPath(dayFolder);

if (folder && folder.children) {
    const mainFile = folder.children.find(f => f.basename === 'main' && f.extension === 'py');
    
    if (mainFile) {
        const content = await app.vault.read(mainFile);
        dv.header(3, 'Caesar Cipher 2/main.py');
        dv.paragraph("```python\n" + content + "\n```");
    } else {
        dv.paragraph("*No se encontró main.py en esta carpeta*");
    }
}
```
```dataviewjs
const dayFolder = "100-days-of-code/Day 8/Caesar Cipher 3";
const folder = app.vault.getAbstractFileByPath(dayFolder);

if (folder && folder.children) {
    const mainFile = folder.children.find(f => f.basename === 'main' && f.extension === 'py');
    
    if (mainFile) {
        const content = await app.vault.read(mainFile);
        dv.header(3, 'Caesar Cipher 3/main.py');
        dv.paragraph("```python\n" + content + "\n```");
    } else {
        dv.paragraph("*No se encontró main.py en esta carpeta*");
    }
}
```

```dataviewjs
const dayFolder = "100-days-of-code/Day 8/Caesar Cipher 12";
const folder = app.vault.getAbstractFileByPath(dayFolder);

if (folder && folder.children) {
    const mainFile = folder.children.find(f => f.basename === 'main' && f.extension === 'py');
    
    if (mainFile) {
        const content = await app.vault.read(mainFile);
        dv.header(3, 'main.py');
        dv.paragraph("```python\n" + content + "\n```");
    } else {
        dv.paragraph("*No se encontró main.py en esta carpeta*");
    }
}
```
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
