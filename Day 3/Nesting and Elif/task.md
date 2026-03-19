### Nested conditionals
You can put if/else statements inside other if/else statements. This is known as nesting.
e.g.

```
if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
if english_score >= 90:
    print("You're good at english)
```

In this case only when a student has over 90 on maths and english, do they get "You are good at everything".

Note: You can also have if statements that don't have a paired else statement.

## Archivos del ejercicio del concepto

[[100-days-of-code/Day 3/Nesting and Elif/task.py|task]] · [[100-days-of-code/Day 3/Nesting and Elif/solution.py|solution]]

> [!info]- Archivos info del ejercicio para PyCharm
> [[100-days-of-code/Day 3/Nesting and Elif/task-info.yaml|info]] · [[100-days-of-code/Day 3/Nesting and Elif/task-remote-info.yaml|remote-info]]
