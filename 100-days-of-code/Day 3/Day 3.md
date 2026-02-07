# Day 3 - Control Flow

← [[100-days-of-code/Day 2/Day 2|Day 2]] | [[100-days-of-code/Day 4/Day 4|Day 4]] →

---
## 📝 ¿Qué conceptos aprendí hoy?

If/else, operadores lógicos, comparaciones, modulo

---
## 🔗 Conceptos relacionados

Este día usa conceptos de:
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Variables para almacenar valores a comparar
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Input para recibir datos del usuario
- [[100-days-of-code/Day 2/Day 2|Day 2]] - Operaciones matemáticas en las comparaciones
- [[100-days-of-code/Day 2/Day 2|Day 2]] - Type conversion para comparar correctamente

---
## 💻 Código del día

```dataviewjs
const dayFolder = "100-days-of-code/Day 3/Treasure Island Project";
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
