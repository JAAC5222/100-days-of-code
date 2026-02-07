# Day 10 - Calculator

← [[100-days-of-code/Day 9/Day 9|Day 9]] | [[100-days-of-code/Day 11/Day 11|Day 11]] →

---
## 📝 ¿Qué aprendí hoy?
Return values, docstrings, recursión

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 6/Day 6|Day 6]] - Funciones con return values
- [[100-days-of-code/Day 9/Day 9|Day 9]] - Diccionarios para operaciones matemáticas
- [[100-days-of-code/Day 5/Day 5|Day 5]] - Loops para continuar calculando
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Control flow para validaciones
- [[100-days-of-code/Day 2/Day 2|Day 2]] - Operaciones matemáticas
---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 10/Calculator Project";
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
- Funciones con `return` tienen sentido: procesan algo y lo devuelven
- Combinar funciones en un programa más grande
### ¿Qué fue difícil?
- Entender qué es lo que devuelve `return` vs solo hacer `print()`
- Docstrings parecen comentarios pero son diferentes
- La recursión (llamar a la función desde sí misma)
### ¿Qué aprendí?
- `return` es como "la respuesta" que da la función
- Los docstrings documentan qué hace la función
- Sin `return`, la función devuelve `None`
---
## 🏷️ Tags

#functions #return #docstrings #project #beginner

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]
