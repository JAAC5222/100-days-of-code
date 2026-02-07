# Day 15 - Coffee Machine (Procedural)

← [[100-days-of-code/Day 14/Day 14|Day 14]] | [[100-days-of-code/Day 16/Day 16|Day 16]] →

---
## 📝 ¿Qué aprendí hoy?

Dictionaries, funciones, while loops, procedural programming

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 9/Day 9|Day 9]] - Diccionarios para recursos y menú
- [[100-days-of-code/Day 6/Day 6|Day 6]] - Funciones para cada acción (report, check_resources, etc.)
- [[100-days-of-code/Day 5/Day 5|Day 5]] - While loops para el menú infinito
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Control flow para validaciones complejas
- [[100-days-of-code/Day 2/Day 2|Day 2]] - Operaciones matemáticas para dinero y recursos
---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 15/Coffee Machine Project";
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
- Diccionarios para recursos (agua, leche, café)
- La lógica de "¿hay suficientes recursos?"
### ¿Qué fue difícil?
- Manejar TODOS los casos: ordenar, reportar recursos, apagar
- Validar que el usuario meta dinero suficiente
- Calcular cambio correctamente
### ¿Qué aprendí?
- Los programas reales tienen muchos "edge cases" (casos especiales)
- While True + break es útil para menús infinitos
- Funciones helper (pequeñas funciones que hacen una cosa) mantienen el código limpio
---
## 🏷️ Tags

#dictionaries #functions #loops #project #beginner

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] |  [[MOC - Projects]]
