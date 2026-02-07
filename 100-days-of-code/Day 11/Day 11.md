# Day 11 - Blackjack

← [[100-days-of-code/Day 10/Day 10|Day 10]] | [[100-days-of-code/Day 12/Day 12|Day 12]] →

---
## 📝 ¿Qué aprendí hoy?
Listas, funciones, lógica compleja, random

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 6/Day 6|Day 6]] - Múltiples funciones trabajando juntas
- [[100-days-of-code/Day 4/Day 4|Day 4]] - Listas para las cartas y random.choice()
- [[100-days-of-code/Day 5/Day 5|Day 5]] - Loops para calcular sumas
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Control flow complejo para la lógica del juego
- [[100-days-of-code/Day 2/Day 2|Day 2]] - Operaciones matemáticas para sumar cartas
---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 11/task";
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
- El concepto del juego es claro
### ¿Qué fue difícil?
- La lógica del juego es compleja: cuándo pedir carta, cuándo parar
- Manejar el As (puede valer 1 u 11 según convenga)
- Coordinar todas las funciones para que trabajen juntas
### ¿Qué aprendí?
- Proyectos complejos necesitan ser divididos en partes pequeñas
- Escribir las funciones primero (aunque estén vacías) ayuda a planear
- Testing: probar cada función por separado antes de unir todo
---
## 🏷️ Tags

#lists #functions #game #project #beginner 

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]
