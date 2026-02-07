# Day 1 - Band Name Generator

[[100-days-of-code/Day 2/Day 2|Day 2]] →

---
## 📝 ¿Qué conceptos aprendí hoy?
inputs, print, string, variables.

---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 1/task";
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
- Print es muy simple, básicamente "mostrar en pantalla"
- Input también es intuitivo, le preguntas algo al usuario
### Observaciones
- Variables son como cajas con etiquetas
- Concatenar strings con `+` es como pegar textos
- El orden importa: primero defines, luego usas

---
## 🏷️ Tags

#variables #strings #input #project #beginner

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]
