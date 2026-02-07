# 🎯 MOC - Programación Orientada a Objetos

Mapa de contenido con todo sobre clases, objetos y OOP en Python.

---
## 🎯 ¿Qué encontrarás aquí?

Este MOC organiza todos los días donde aprendí Programación Orientada a Objetos: clases, objetos, métodos, atributos, herencia, y más.

---
## 📚 Introducción a OOP
Los primeros pasos en el paradigma orientado a objetos.
- [[100-days-of-code/Day 16/Day 16|Day 16]] - Introducción a OOP: Clases, Objetos, Métodos, Atributos
- [[100-days-of-code/Day 17/Day 17|Day 17]] - Creando tus propias clases (Quiz Game)

**¿Por qué OOP?**
- Organizar código de forma más natural (como objetos del mundo real)
- Reutilizar código más fácilmente
- Código más mantenible y escalable
---
## 🏗️ Conceptos Fundamentales
### Clases (Classes)
**Definición**: Una clase es como un "molde" o "plano" para crear objetos.
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!")
```

**Días donde lo usé:**
- [[100-days-of-code/Day 16/Day 16|Day 16]] - Usando clases de otros (CoffeeMaker, Menu)
- [[100-days-of-code/Day 17/Day 17|Day 17]] - Creando mis propias clases
---
### Objetos (Objects)
**Definición**: Un objeto es una **instancia** de una clase. Es la "cosa real" creada a partir del molde.
```python
my_dog = Dog("Rex")  # my_dog es un objeto de la clase Dog
```

**Concepto clave:**
- Una clase puede crear múltiples objetos
- Cada objeto tiene sus propios valores (atributos)
---
### Atributos (Attributes)
**Definición**: Variables que pertenecen a un objeto.
```python
class Car:
    def __init__(self, color, brand):
        self.color = color    # Atributo
        self.brand = brand    # Atributo
```

**Días donde lo usé:**
- [[100-days-of-code/Day 16/Day 16|Day 16]] - Accediendo atributos de objetos
- [[100-days-of-code/Day 17/Day 17|Day 17]] - Creando mis propios atributos
---
### Métodos (Methods)
**Definición**: Funciones que pertenecen a una clase/objeto.
```python
class Calculator:
    def add(self, a, b):     # Método
        return a + b
```

**Conceptos clave:**
- `self` siempre es el primer parámetro
- `self` se refiere al objeto que llama al método
- Métodos pueden acceder a los atributos del objeto
---
### Constructor `__init__()`
**Definición**: Método especial que se ejecuta automáticamente al crear un objeto.
```python
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age
```

**Para qué sirve:**
- Inicializar atributos del objeto
- Configurar el estado inicial del objeto
---
## 🔗 Comparación: Procedural vs OOP

### Procedural Programming (Días 1-15)
```python
# Variables sueltas
coffee_price = 2.50
water = 300
milk = 200

# Funciones separadas
def make_coffee():
    # ...
    pass

def check_resources():
    # ...
    pass
```
### Object-Oriented Programming (Día 16+)
```python
# Todo organizado en clases
class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
    
    def make_coffee(self):
        # ...
        pass
    
    def check_resources(self):
        # ...
        pass

# Crear objeto
my_machine = CoffeeMachine()
```

**Ventajas de OOP:**
- ✅ Datos y funciones relacionadas juntas
- ✅ Múltiples objetos independientes
- ✅ Código más organizado y reutilizable
---
## 🚀 Proyectos con OOP

| Día | Proyecto | Qué aprendí |
|-----|----------|-------------|
| [[100-days-of-code/Day 16/Day 16\|Day 16]] | Coffee Machine (OOP version) | Usar clases de otros, import clases |
| [[100-days-of-code/Day 17/Day 17\|Day 17]] | Quiz Game | Crear mis propias clases desde cero |

---
## 🎓 Conceptos Avanzados (Próximamente)

- **Herencia** - Clases que heredan de otras
- **Polimorfismo** - Mismo método, diferentes comportamientos
- **Encapsulación** - Ocultar datos internos
- **Métodos especiales** - `__str__`, `__repr__`, `__len__`, etc.
---
## 📊 Progreso en OOP
```dataview
TABLE WITHOUT ID
  file.link as "Día",
  tags as "Conceptos"
FROM "100-days-of-code"
WHERE contains(tags, "#OOP")
SORT file.name ASC
```

---
## 💡 Tips para entender OOP
1. **Piensa en objetos del mundo real**: Una clase Dog es como "la idea de un perro", un objeto es un perro específico como "Rex"
2. **self es la clave**: Siempre pregúntate "¿de qué objeto estoy hablando?"
3. **No tengas miedo**: OOP parece raro al principio, pero con práctica se vuelve natural
4. **Practica creando clases**: La mejor forma de aprender es crear tus propias clases
---
## 🔗 Relacionado con
- [[MOC - Python Fundamentals]] - Los fundamentos que necesitas saber antes de OOP
- [[MOC - Projects]] - Proyectos que usan OOP
---
**Tags relacionados**: #OOP #classes #objects #methods #attributes #intermediate

**Última actualización**: Day 17