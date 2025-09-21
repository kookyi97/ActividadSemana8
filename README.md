
<p align="center">
  <img src="https://sgc.ugb.edu.sv/wp-content/uploads/2024/10/UGB_LOGO.png" alt="UGB" width="200">
</p>

# ActividadSemana8

Repositorio de la Actividad Sumativa Semana 8

---

## Proyecto: Recordatorio de Medicamentos  

### Autores:
- *Mayerlin Yisel Aguilar Cruz - SMSS067424*  
- *Marleny Jamileth Martínez Méndez - SMSS018924*

---

## 1. Planteamiento de la problemática

Muchas personas olvidan tomar sus medicamentos a tiempo. Esto puede ser muy peligroso en el caso de tratamientos médicos, ya que la falta de disciplina en la toma de medicamentos afecta directamente la salud.  

Por eso, es útil contar con una aplicación de recordatorio de medicamentos, donde el usuario pueda registrar el nombre del medicamento, la hora a la que debe tomarlo y la dosis. La aplicación mostrará una lista de medicamentos y permitirá tener control de los horarios.

---

## 2. Solución planteada

La aplicación desarrollada en *Python con PyQt5* permite:  

- Ingresar el *nombre del medicamento*.  
- Ingresar la *dosis* (ejemplo: 1 tableta, 5 ml, etc.).  
- Ingresar la *hora programada* mediante un campo de selección de hora.  
- Guardar el medicamento en una lista de recordatorios.  
- Mostrar todos los medicamentos pendientes en un listado.  
- Limpiar la lista cuando se necesite reiniciar.  

De esta manera, se facilita el cumplimiento de tratamientos médicos y se ayuda a las personas a mantener un control más estricto de sus medicinas.  

---

## 3. Descripción del programa

Este programa cuenta con una interfaz gráfica creada en *PyQt5*, donde se incluyen al menos cinco widgets básicos:  

- *QLabel* (etiquetas).  
- *QLineEdit* (campos de entrada de texto).  
- *QPushButton* (botones).  
- *QTimeEdit* (selector de hora).  
- *QListWidget* (lista de recordatorios).  

El sistema incluye:  
- *Validaciones* para evitar registros incompletos.  
- *Notificaciones emergentes* (QMessageBox) cuando llega la hora programada.  
- La posibilidad de *agregar, eliminar o limpiar* la lista de medicamentos.  
- Un *temporizador (QTimer)* que revisa automáticamente los recordatorios cada minuto.

---

