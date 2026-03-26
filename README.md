# 📦 Sistema de Respaldos en Python

> Automatiza copias de seguridad de carpetas con múltiples modos: por días, por horas, continuo o con historial.

---

## 🧠 Descripción

El módulo implementa una clase `Respaldo` que permite copiar una carpeta de origen a un destino de forma automática usando diferentes estrategias de programación.

---

## ⚙️ Características

- Copia completa de carpetas
- Programación por días
- Ejecución por hora específica
- Ejecución por múltiples horas
- Respaldo continuo
- Historial automático

---

## 🧩 Clase `Respaldo`

### Inicialización

```python
Respaldo(ruta_origen, ruta_destino)
```

---

## 🛠️ Configuración

### Establecer días

```python
r.establecer_dia("lunes")
r.establecer_dia("viernes")
```

### Establecer hora

```python
r.establecer_hora("14:00")
```

### Configurar múltiples horas

```python
r.configurar_horas([0, 12, 18])
```

---

## 🚀 Métodos principales

### Respaldo manual

```python
r.respaldo(existe=True)
```

### Respaldo por días

```python
r.respaldo_programado_dias()
```

### Respaldo cada hora

```python
r.respaldo_cada_hora()
```

### Respaldo por horas

```python
r.respaldo_por_horas()
```

### Respaldo con historial

```python
r.respaldo_continuo_historial()
```

---

## 📌 Ejemplos

### Ejemplo 1: Básico

```python
from respaldo import Respaldo

r = Respaldo("C:/datos", "D:/backup")
r.respaldo(existe=True)
```

---

### Ejemplo 2: Por días

```python
r.establecer_dia("lunes")
r.establecer_hora("10:00")
r.respaldo_programado_dias()
```

---

### Ejemplo 3: Cada hora

```python
r.respaldo_cada_hora()
```

---

### Ejemplo 4: Horas específicas

```python
r.configurar_horas([6, 12, 18])
r.respaldo_por_horas()
```

---

### Ejemplo 5: Historial

```python
r.respaldo_continuo_historial()
```

---

## ⚠️ Recomendaciones

- Usar rutas absolutas
- Ejecutar como servicio
- Agregar logs en producción
