We're going to build a tip calculator.

If the bill was $150.00, split between 5 people, with 12% tip. 

Each person should pay:

`(150.00 / 5) * 1.12 = 33.6`

After formatting the result to 2 decimal places = `33.60`

## Demo
https://appbrewery.github.io/python-day2-demo/

### Very Optional Reading: Floating Point Arithmetic
https://docs.python.org/3/tutorial/floatingpoint.html

---
## Solution Code
```dataviewjs
const file = app.vault.getAbstractFileByPath("Day 2/Tip Calculator Project/task.py"); const content = await app.vault.read(file); dv.paragraph("```python\n" + content + "\n```");
```
