# Day {{DAY_NUMBER}} - {{PROJECT_NAME}}

← [[100-days-of-code/Day {{PREV_DAY}}/Day {{PREV_DAY}}|Day {{PREV_DAY}}]] | [[100-days-of-code/Day {{NEXT_DAY}}/Day {{NEXT_DAY}}|Day {{NEXT_DAY}}]] →

---
## 📝 ¿Qué aprendí hoy?

{{MAIN_CONCEPT}}

---
## 🔗 Conceptos relacionados

Este día usa conceptos de:
- [[100-days-of-code/Day X/Day X|Day X]] - {{CONCEPTO_RELACIONADO}}

---
## 💻 Código del día
````dataviewjs
const dayFolder = "100-days-of-code/Day {{DAY_NUMBER}}";
const folder = app.vault.getAbstractFileByPath(dayFolder);

if (folder && folder.children) {
    const pyFiles = folder.children.filter(f => f.extension === 'py');
    
    if (pyFiles.length > 0) {
        for (let file of pyFiles) {
            const content = await app.vault.read(file);
            dv.header(3, file.basename + '.py');
            dv.paragraph("```python\n" + content + "\n```");
            dv.paragraph("---");
        }
    } else {
        dv.paragraph("*No hay archivos .py en este día*");
    }
}
````
````dataviewjs
const dayFolder = "100-days-of-code/Day 16/src"; const folder = app.vault.getAbstractFileByPath(dayFolder); if (folder && folder.children) { const pyFiles = folder.children.filter(f => f.extension === 'py'); if (pyFiles.length > 0) { pyFiles.sort((a, b) => { if (a.basename === 'main') return -1; if (b.basename === 'main') return 1; return a.basename.localeCompare(b.basename); }); for (let file of pyFiles) { const content = await app.vault.read(file); dv.header(3, file.basename + '.py'); dv.paragraph("```python\n" + content + "\n```"); dv.paragraph("---"); } } else { dv.paragraph("*No hay archivos .py directamente en esta carpeta*"); } }
````
---
## 🧠 Reflexión
### ¿Qué fue fácil?
- 
### ¿Qué fue difícil?
- 
### ¿Qué aprendí?
- 
---
## 🏷️ Tags

---
**MOCs relacionados**: [[MOC - OOP]] | [[MOC - Projects]]
