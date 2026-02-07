# Day 16 - Coffee Machine (OOP)

← [[100-days-of-code/Day 15/Day 15|Day 15]] | [[100-days-of-code/Day 17/Day 17|Day 17]] →

---
## 📝 ¿Qué aprendí hoy?
Clases, objetos, métodos, atributos, importar clases

---
## 🔗 Conceptos relacionados
Este día usa conceptos de:
- [[100-days-of-code/Day 6/Day 6|Day 6]] - Métodos son funciones dentro de clases
- [[100-days-of-code/Day 9/Day 9|Day 9]] - Atributos son como diccionarios de cada objeto
- [[100-days-of-code/Day 15/Day 15|Day 15]] - Misma funcionalidad pero con paradigma diferente
- [[100-days-of-code/Day 1/Day 1|Day 1]] - Variables ahora son atributos de objetos
---
## 💻 Código del día
```dataviewjs
const dayFolder = "100-days-of-code/Day 16/src"; const folder = app.vault.getAbstractFileByPath(dayFolder); if (folder && folder.children) { const pyFiles = folder.children.filter(f => f.extension === 'py'); if (pyFiles.length > 0) { pyFiles.sort((a, b) => { if (a.basename === 'main') return -1; if (b.basename === 'main') return 1; return a.basename.localeCompare(b.basename); }); for (let file of pyFiles) { const content = await app.vault.read(file); dv.header(3, file.basename + '.py'); dv.paragraph("```python\n" + content + "\n```"); dv.paragraph("---"); } } else { dv.paragraph("*No hay archivos .py directamente en esta carpeta*"); } }
```

---
## 🧠 Reflexión
### ¿Qué fue fácil?
- El concepto de "objetos como cosas del mundo real"
- Importar clases de otros archivos
### ¿Qué fue difícil?
- Entender qué es `self` y por qué está en todos lados
- Diferenciar entre métodos (funciones de la clase) y funciones normales
### ¿Qué aprendí?
- OOP organiza código en "objetos" que tienen datos y funciones relacionadas
- Las clases son como "moldes" y los objetos son las "cosas creadas con el molde"
- OOP hace el código más fácil de entender y mantener
---
## 🏷️ Tags

#OOP #classes #objects #methods #project #intermediate

---
**MOCs relacionados**: [[MOC - OOP]] | [[MOC - Projects]]
