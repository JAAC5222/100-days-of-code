Playing computer is an important skill in debugging. You need to be able to go through your code line by line as if you were the computer to help you figure out what is going wrong. 

### PAUSE 1
Play computer and go through the code line by line as if you were executing the code to figure out why 1994 does not work as expected. Then go ahead and fix the code.

---
## Solution Code
```dataviewjs
const file = app.vault.getAbstractFileByPath("Day 13/Play Computer/task.py"); const content = await app.vault.read(file); dv.paragraph("```python\n" + content + "\n```");
```
