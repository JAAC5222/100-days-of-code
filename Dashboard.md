# 🏠 Dashboard - 100 Days of Code

---
## 📊 Mi Progreso

| Métrica              | Valor      |
| -------------------- | ---------- |
| **Día actual**       | [[Day 17]] |
| **Días completados** | 17 / 100   |
| **Porcentaje**       | 17%        |
| **Racha actual**     | 🔥 17 días |

---
## 🗺️ Mapas de Contenido (MOCs)

Mis guías organizadas por tema:

- 📘 [[MOC - Python Fundamentals]] - Conceptos básicos de Python
- 🎯 [[MOC - OOP]] - Programación Orientada a Objetos
- 🚀 [[MOC - Projects]] - Todos mis proyectos completados

---
## 📅 Últimos 5 Días
```dataview
TABLE WITHOUT ID
  file.link as "Día",
  tags as "Tags"
FROM "100-days-of-code"
WHERE file.name != "100-days-of-code"
SORT file.name DESC
LIMIT 5
```

---
## 🎯 Objetivos Actuales

- [ ] Completar módulo de OOP (Días 16-20)
- [ ] Hacer primer proyecto con API
- [ ] Aprender list comprehensions
- [ ] Construir un juego completo

---
## 🔥 Conceptos que Domino
```dataview
TABLE WITHOUT ID
  rows.file.link as "Días donde lo usé"
FROM "100-days-of-code"
WHERE file.name != "100-days-of-code"
FLATTEN tags as tag
WHERE tag = "#OOP" OR tag = "#functions" OR tag = "#loops"
GROUP BY tag
```

---
## 📚 Recursos Útiles

- [Documentación Python](https://docs.python.org/3/)
- [[_Tag System.md]]- Mi sistema de organización
- [100 Days of Code - Udemy](https://www.udemy.com/course/100-days-of-code/)

---
## 🧠 Reflexión Semanal

### Semana 3 (Días 15-21)
**Logros**: Entendí OOP, creé mi primer juego con clases
**Desafíos**: Los métodos con `self` todavía me confunden a veces
**Siguiente**: Profundizar en herencia y polimorfismo

---
**Última actualización**: Day 17 - Quiz Game

> [!info] Documento de información para PyCharm
> [[course-info.yaml]]
> 