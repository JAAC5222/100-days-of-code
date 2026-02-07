# Day 7 - Hangman Game

← [[100-days-of-code/Day 6/Day 6|Day 6]] | [[100-days-of-code/Day 8/Day 8|Day 8]] →

---
## 📝 ¿Qué conceptos aprendí hoy?
Loops, listas, strings, lógica de juego

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 4/Day 4|Day 4]] - Listas para palabras y letras adivinadas
- [[100-days-of-code/Day 5/Day 5|Day 5]] - Loops para iterar sobre letras
- [[100-days-of-code/Day 6/Day 6|Day 6]] - Funciones para organizar el código
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Control flow para validar letras
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Strings para manipular palabras

---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 7"; const folder = app.vault.getAbstractFileByPath(dayFolder); if (folder && folder.children) {  const conceptFolders = folder.children.filter(f => f.children && f.name !== 'task' && !f.name.endsWith('.yaml') && f.children.some(file => file.basename === 'task' && file.extension === 'md') ); if (conceptFolders.length > 0) {  conceptFolders.sort((a, b) => a.name.localeCompare(b.name)); const links = conceptFolders.map(folder => { const taskMd = folder.children.find(f => f.basename === 'task' && f.extension === 'md'); return `[[${taskMd.path}|${folder.name}]]`; }).join(' • '); dv.paragraph(links); } else { dv.paragraph("*No hay conceptos adicionales este día*"); } }
```
```dataviewjs
const dayFolder = "100-days-of-code/Day 7/task";
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
- El ASCII art hace el formato más atractivo
### ¿Qué fue difícil?
- Combinar TODO lo aprendido hasta ahora en un proyecto real
- La lógica de reemplazar guiones bajos con letras correctas
### ¿Qué aprendí?
- Planear antes de codear ahorra tiempo
- Está bien googlear y pedir ayuda
---
## 🏷️ Tags

#loops #lists #strings #game #project #beginner

---

**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - OOP]] | [[MOC - Projects]]
