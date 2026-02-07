# Day 4 - Lists & Randomisation

← [[100-days-of-code/Day 3/Day 3|Day 3]] | [[100-days-of-code/Day 5/Day 5|Day 5]] →

---
## 📝 ¿Qué conceptos aprendí hoy?
Listas, indexing, IndexError, random module

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Variables para almacenar listas
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Control flow para validaciones
- [[100-days-of-code/Day 2/Day 2|Day 2]] - Operaciones con índices numéricos
---
## 💻 Código del día

```dataviewjs
const dayFolder = "100-days-of-code/Day 4/Rock Paper Scissors";
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
