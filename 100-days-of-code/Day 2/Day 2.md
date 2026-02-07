# Day 2 - Data Types & Operations

← [[100-days-of-code/Day 1/Day 1|Day 1]] | [[100-days-of-code/Day 3/Day 3|Day 3]] →

---
## 📝 ¿Qué conceptos aprendí hoy?
Data types, type conversion, mathematical operations

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Variables y strings para almacenar y manipular datos
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Input para recibir datos del usuario

---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 2/Tip Calculator Project";
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

- Operaciones matemáticas básicas (+, -,\*, /)
- El concepto de diferentes tipos de datos tiene sentido
### Observaciones

- Type casting es básicamente "convertir de un tipo a otro"

---
## 🏷️ Tags

#variables #operators #data-types #exercise #beginner

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]
