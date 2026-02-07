# 🐍 MOC - Python Fundamentals

Mapa de contenido con todos los conceptos fundamentales de Python que he aprendido.

---
## 🎯 ¿Qué encontrarás aquí?

Este MOC organiza todos los días donde aprendí conceptos básicos de Python: variables, tipos de datos, estructuras de control, funciones, y estructuras de datos.

---
## 📦 Variables y Tipos de Datos

Los primeros pasos en Python.

- [[Day 1]] - Printing, Inputs, Variables básicas (Band Name Generator)
- [[100]] - Data Types, Mathematical Operations, Number Manipulation

**Conceptos clave aprendidos:**
- Variables son como cajas que guardan información
- Python es dynamically typed (no necesitas declarar tipos)
- Operaciones matemáticas básicas (+, -,\*, /, //, %,\*\*)
- Input siempre devuelve string
---
## 🔀 Control de Flujo

Cómo hacer que tu código tome decisiones.
### Condicionales
- [[Day 3]] - If/Else, Logical Operators (and, or, not), Modulo
### Loops
- [[Day 5]] - For Loops, Range, iteración sobre listas
- [[Day 7]] - Aplicación práctica de loops (proyecto Hangman)

**Conceptos clave aprendidos:**
- If/else para decisiones
- For loops para iterar sobre secuencias
- Range() para generar secuencias de números
- Break y continue para controlar loops

---
## 📝 Estructuras de Datos

Las herramientas para organizar información.
### Listas
- [[Day 4]] - Lists, Indexing, IndexError, métodos básicos
- [[Day 5]] - Iteración sobre listas con for loops
### Diccionarios
- [[Day 9]] - Dictionaries, key-value pairs, Nested Lists and Dictionaries (Blind Auction)

**Conceptos clave aprendidos:**
- Listas: ordenadas, mutables, permiten duplicados
- Indexing empieza en 0
- Diccionarios: key-value pairs, super rápidos para búsquedas
- Estructuras anidadas (listas dentro de diccionarios, etc.)
---
## ⚙️ Funciones
Código reutilizable y modular.
- [[Day 6]] - Funciones básicas, definición y llamada
- [[Day 8]] - Funciones con parámetros (Caesar Cipher)
- [[Day 10]] - Functions with Outputs, Return values, Docstrings (Calculator)

**Conceptos clave aprendidos:**
- Funciones = DRY (Don't Repeat Yourself)
- def para definir funciones
- Parámetros vs argumentos
- `return` devuelve valores
- Docstrings para documentar funciones
---
## 🔍 Scope
Dónde viven las variables.
- [[Day 12]] - Block Scope, Global Variables, Global Constants, Local vs Global

**Conceptos clave aprendidos:**
- Variables locales solo existen dentro de funciones
- Variables globales accesibles en todo el programa
- Usar MAYÚSCULAS para constantes globales
- Evitar modificar variables globales desde funciones
---
## 🐛 Debugging
Cómo encontrar y arreglar errores.
- [[100-days-of-code/Day 13/Day 13]] - Describe the Problem, Fix the Errors, Play Computer

**Conceptos clave aprendidos:**
- Leer mensajes de error con calma
- Usar print() para debug
- "Play computer" (ejecutar código mentalmente)
- Revisar indentación y sintaxis
---
## 🎮 Proyectos que usan Fundamentos
```dataview
TABLE WITHOUT ID
  file.link as "Día",
  tags as "Conceptos"
FROM "100-days-of-code"
WHERE contains(file.name, "Day 1") OR contains(file.name, "Day 2") OR contains(file.name, "Day 3") OR contains(file.name, "Day 4") OR contains(file.name, "Day 5") OR contains(file.name, "Day 6") OR contains(file.name, "Day 7") OR contains(file.name, "Day 8") OR contains(file.name, "Day 9") OR contains(file.name, "Day 10") OR contains(file.name, "Day 11") OR contains(file.name, "Day 12") OR contains(file.name, "Day 13") OR contains(file.name, "Day 14") OR contains(file.name, "Day 15")
SORT file.name ASC
```
---
## 🚀 Proyectos Principales (Días 1-15)

| Día        | Proyecto            | Conceptos Clave                    |
| ---------- | ------------------- | ---------------------------------- |
| [[Day 1]]  | Band Name Generator | Variables, input, strings          |
| [[Day 7]]  | Hangman             | Loops, listas, strings             |
| [[Day 8]]  | Caesar Cipher       | Funciones, parámetros, loops       |
| [[Day 9]]  | Blind Auction       | Dictionaries, clear screen         |
| [[Day 10]] | Calculator          | Return values, recursión           |
| [[Day 11]] | Blackjack           | Listas, funciones, lógica compleja |
| [[Day 14]] | Higher or Lower     | Comparaciones, loops               |
| [[Day 15]] | Coffee Machine      | Dictionaries, funciones            |

---
## 📌 Notas Importantes
- Estos son los **building blocks** de todo lo demás
- Si no dominas estos conceptos, OOP y proyectos avanzados serán difíciles
- Los días 1-15 son la base sólida antes de OOP
---
## ➡️ ¿Qué sigue?

Después de dominar estos fundamentos, continuamos con:
- [[MOC - OOP]] - Programación Orientada a Objetos (Day 16+)
- Módulos y Packages avanzados
- Manejo de archivos y APIs
---

**Tags relacionados**: #variables #control-flow #functions #lists #dictionaries #beginner

**Última actualización**: Day 17