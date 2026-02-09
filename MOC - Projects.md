# 🚀 MOC - Proyectos Completados

Lista de todos los proyectos del bootcamp 100 Days of Code.

---
## 🎯 ¿Qué encontrarás aquí?
Este MOC organiza todos los proyectos completos que he construido, agrupados por nivel de dificultad y tipo.

---
## 🟢 Beginner Projects
Proyectos fundamentales usando conceptos básicos de Python.
### 🎮 Juegos

| Día | Proyecto | Conceptos Principales | Dificultad |
|-----|----------|----------------------|------------|
| [[100-days-of-code/Day 7/Day 7\|Day 7]] | **Hangman** | Loops, listas, strings, ASCII art | ⭐⭐ |
| [[100-days-of-code/Day 11/Day 11\|Day 11]] | **Blackjack** | Listas, funciones, random, game logic | ⭐⭐⭐ |
| [[100-days-of-code/Day 14/Day 14\|Day 14]] | **Higher or Lower** | Comparaciones, loops, data | ⭐⭐ |

### 🛠️ Utilidades y Herramientas

| Día                                        | Proyecto                        | Conceptos Principales           | Dificultad |
| ------------------------------------------ | ------------------------------- | ------------------------------- | ---------- |
| [[100-days-of-code/Day 1/Day 1\|Day 1]]    | **Band Name Generator**         | Variables, input, concatenación | ⭐          |
| [[100-days-of-code/Day 8/Day 8\|Day 8]]    | **Caesar Cipher**               | Funciones, encryption, strings  | ⭐⭐         |
| [[100-days-of-code/Day 9/Day 9\|Day 9]]    | **Blind Auction**               | Dictionaries, clear screen      | ⭐⭐         |
| [[100-days-of-code/Day 10/Day 10\|Day 10]] | **Calculator**                  | Return values, recursión        | ⭐⭐         |
| [[100-days-of-code/Day 15/Day 15\|Day 15]] | **Coffee Machine (Procedural)** | Dictionaries, while loops       | ⭐⭐⭐        |

---
## 🟡 Intermediate Projects

Proyectos que introducen conceptos más avanzados.
### 🎯 Programación Orientada a Objetos

| Día | Proyecto | Conceptos Principales | Dificultad |
|-----|----------|----------------------|------------|
| [[100-days-of-code/Day 16/Day 16\|Day 16]] | **Coffee Machine (OOP)** | Clases, objetos, imports | ⭐⭐⭐ |
| [[100-days-of-code/Day 17/Day 17\|Day 17]] | **Quiz Game** | Clases propias, métodos, atributos | ⭐⭐⭐ |

### 🌐 APIs y Web 
*Proyectos con APIs, requests, JSON, web scraping*

### 🎨 GUI y Visualización
*Proyectos con Tkinter, Turtle, gráficas*

---
## 🔴 Advanced Projects
**Próximamente** - Proyectos complejos con múltiples tecnologías.

---
## 📊 Todos los proyectos por tag
### Por nivel de dificultad
```dataview
TABLE WITHOUT ID
  file.link as "Day",
  tags as "Tags"
FROM "100-days-of-code"
WHERE contains(tags, "#project") AND contains(tags, "#beginner")
SORT file.name ASC
```

### Proyectos Intermediate
```dataview
TABLE WITHOUT ID
  file.link as "Día",
  tags as "Tags"
FROM "100-days-of-code"
WHERE contains(tags, "#project") AND contains(tags, "#intermediate")
SORT file.name ASC
```

### Proyectos Advanced
```dataview
TABLE WITHOUT ID
  file.link as "Día",
  tags as "Tags"
FROM "100-days-of-code"
WHERE contains(tags, "#project") AND contains(tags, "#advanced")
SORT file.name ASC
```

---
## 🏆 Proyectos Favoritos
*(Actualizar conforme avance)*

1. 

---
## 💡 Reflexiones sobre proyectos
### ¿Qué hace un buen proyecto?
- **Combina múltiples conceptos** aprendidos en días anteriores
- **Tiene un propósito claro** y es útil o divertido
- **Es escalable** - puedo agregar features después
- **Me hace pensar** en cómo estructurar el código
### Lecciones aprendidas
- Los proyectos son donde realmente se aprende
- Es normal estar frustrado al inicio de un proyecto
- Dividir el proyecto en partes pequeñas ayuda muchísimo
- Revisar proyectos anteriores es súper útil
---
## 🎯 Por Tecnología/Concepto
### Juegos con Lógica Compleja
- [[100-days-of-code/Day 11/Day 11|Day 11]] - Blackjack
- [[100-days-of-code/Day 17/Day 17|Day 17]] - Quiz Game
- [[100-days-of-code/Day 14/Day 14|Day 14]] - Higher or Lower
### Programación Orientada a Objetos
- [[100-days-of-code/Day 16/Day 16|Day 16]] - Coffee Machine (OOP)
- [[100-days-of-code/Day 17/Day 17|Day 17]] - Quiz Game
### Manipulación de Strings
- [[100-days-of-code/Day 7/Day 7|Day 7]] - Hangman
- [[100-days-of-code/Day 8/Day 8|Day 8]] - Caesar Cipher
### Diccionarios y Estructuras de Datos
- [[100-days-of-code/Day 9/Day 9|Day 9]] - Blind Auction
- [[100-days-of-code/Day 15/Day 15|Day 15]] - Coffee Machine
### Funciones y Return Values
- [[100-days-of-code/Day 10/Day 10|Day 10]] - Calculator
- [[100-days-of-code/Day 8/Day 8|Day 8]] - Caesar Cipher
---
## 🔗 Relacionado con
- [[MOC - Python Fundamentals]] - Conceptos usados en proyectos beginner
- [[MOC - OOP]] - Proyectos que usan OOP
---
**Tags relacionados**: #project #game #automation #OOP

**Última actualización**: Day 17

---
## 📝 Template para nuevos proyectos

Cuando complete un nuevo proyecto, agregar a la tabla correspondiente según su tag:
```markdown
| [[100-days-of-code/Day X/Day X|Day X]] | **Nombre** | Conceptos | ⭐⭐⭐ |
```

Y actualizar las reflexiones si el proyecto fue particularmente interesante.