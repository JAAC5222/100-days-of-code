# Day 9 - Blind Auction

← [[100-days-of-code/Day 8/Day 8|Day 8]] | [[100-days-of-code/Day 10/Day 10|Day 10]] →

---
## 📝 ¿Qué conceptos aprendí hoy?
Dictionaries, nested structures, clear screen

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 6/Day 6|Day 6]] - Funciones para organizar la lógica
- [[100-days-of-code/Day 5/Day 5|Day 5]] - Loops para iterar sobre diccionarios
- [[100-days-of-code/Day 3/Day 3|Day 3]] - Control flow para determinar el ganador
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Input para nombres y ofertas
---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 9/Blind Auction Project";
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
- Los diccionarios son como listas pero con "etiquetas" en lugar de números
- Key-value pairs tienen mucho sentido: nombre → valor
### ¿Qué fue difícil?
- Sintaxis de diccionarios: `{}` vs `[]
- Iterar sobre diccionarios con `.items()`, `.keys()`, `.values()`
### ¿Qué aprendí?
- Los diccionarios son perfectos para datos estructurados
- Puedes tener listas dentro de diccionarios y viceversa
- `clear()` para limpiar la consola hace el programa más dinámico
---
## 🏷️ Tags

#dictionaries #structures #project #beginner

---
**MOCs relacionados**: [[MOC - Python Fundamentals]] | [[MOC - Projects]]
