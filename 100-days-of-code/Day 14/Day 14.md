# Day 14 - Higher or Lower

← [[100-days-of-code/Day 13/Day 13|Day 13]] | [[100-days-of-code/Day 15/Day 15|Day 15]] →

---
## 📝 ¿Qué aprendí hoy?

Comparaciones, loops, game logic

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 9/Day 9|Day 9]] - Diccionarios para almacenar datos del juego
- [[100-days-of-code/Day 6/Day 6|Day 6]] - Funciones para organizar la lógica
- [[100-days-of-code/Day 5/Day 5|Day 5]] - While loops para el game loop
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Comparaciones para determinar ganador
- [[100-days-of-code/Day 4/Day 4|Day 4]] - Random para seleccionar celebridades
---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 14/Higher or Lower Project";
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
- Importar datos de otro archivo (`game_data.py`)
### ¿Qué fue difícil?
- Manejar el "game loop" (que el juego continúe hasta perder)
- Hacer que el ganador de la ronda anterior sea el "A" de la siguiente
- Diseñar la interfaz de usuario en terminal
### ¿Qué aprendí?
- Los juegos son proyectos perfectos para practicar loops y lógica
- Separar datos (game_data) de lógica (main.py) es buena práctica
- Los while loops son mejores para "repetir hasta que pase X"
---
## 🏷️ Tags

#game #loops #conditionals #project #beginner

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]
