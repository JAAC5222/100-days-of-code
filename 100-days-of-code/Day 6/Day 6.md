# Day 6 - Functions

← [[100-days-of-code/Day 5/Day 5|Day 5]] | [[100-days-of-code/Day 7/Day 7|Day 7]] →

---
## 📝 ¿Qué conceptos aprendí hoy?
Definir funciones, llamar funciones, indentación

---
## 🔗 Conceptos relacionados
Este día usa conceptos de días anteriores.

---
## 💻 Código del día

```dataviewjs
const dayFolder = "100-days-of-code/Day 6/Functions";
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

- Llamar funciones es como usar comandos: `print()`, `len()`, etc.
- El concepto de "define una vez, usa mil veces"
### ¿Qué aprendí?

- Las funciones hacen el código más organizado y reutilizable
- Los nombres de funciones deben ser descriptivos (no `func1`, `func2`)
- DRY = Don't Repeat Yourself (ahora entiendo por qué las funciones son importantes)
---
## 🏷️ Tags

#functions #def #exercise #beginner

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]
