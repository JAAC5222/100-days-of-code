# Day 12 - Scope

← [[100-days-of-code/Day 11/Day 11|Day 11]] | [[100-days-of-code/Day 13/Day 13|Day 13]] →

---
## 📝 ¿Qué aprendí hoy?
Local vs global scope, constantes globales

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 6/Day 6|Day 6]] - Funciones para entender scope local vs global
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Variables globales y locales
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Block scope con if/else
---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 12/Number Guessing Project";
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
- Variables locales vs globales tiene sentido conceptual
- Las constantes globales en MAYÚSCULAS son buena práctica
### ¿Qué fue difícil?
- Entender POR QUÉ no puedo modificar una variable global desde una función sin `global`
- Scope dentro de scope dentro de scope
- Cuándo crear variables globales vs pasarlas como parámetros
### ¿Qué aprendí?
- Las variables locales "mueren" cuando la función termina
- Variables globales pueden causar bugs si no tienes cuidado
- Es mejor pasar variables como parámetros que usar globales
---
## 🏷️ Tags

#scope #variables #functions #exercise #beginner

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]
