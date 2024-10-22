
# Hack4U Academy Courses Library

Una bibiblioteca python para consultar cursos de hack4you.

## Cursos dsiponibles:

- Introducción a Linux [15 horas]
- Personalización de Linux [3 horas]
- Introducción al Hacking [53 horas]

## Instalación

Instala el paquete usando pip3:

```python3
pip install hack4you
```
## Uso básico:

### Listar todos los cursos

```python
from hack4you import list_courses

for course in list_courses:
    print(course)
```

### Obtener curso por nombre

```python
from hack4you import get_course_by_name
course = get_course_by_name("Introducción a Linux)
print(course)
```

### Total duration

```python3
from hack4you import total_duration
    print(f"El computo de horas totales es de :{total_duration()}")
