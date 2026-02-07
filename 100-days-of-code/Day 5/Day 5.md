# Day 5 - For Loops

← [[100-days-of-code/Day 4/Day 4|Day 4]] | [[100-days-of-code/Day 6/Day 6|Day 6]] →

---
## 📝 ¿Qué conceptos aprendí hoy?
For loops, range(), iteración sobre listas

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 4/Day 4|Day 4]] - Listas para iterar sobre elementos
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Control flow dentro de loops
- [[100-days-of-code/Day 2/Day 2|Day 2]] - Range trabaja con números
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Variables para acumuladores y contadores

---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 5/Password Generator Project";
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

- El concepto de "repetir algo varias veces" es claro
- Iterar sobre una lista es más simple de lo que parece
### Observaciones

- For loops son MUCHO más eficientes que copiar/pegar código 20 veces
- `range(start, stop, step)` es MUY flexible
- Puedes hacer loops dentro de loops
---
## 🏷️ Tags

#loops #for-loop #range #exercise #beginner

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]
