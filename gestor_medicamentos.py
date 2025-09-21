import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QTimeEdit, QListWidget
)

from PyQt5.QtCore import QTime, QTimer

class RecordatorioMedicamentos(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Recordatorio de Medicamentos") 
        self.setGeometry(300, 200, 500, 400) 

        # --- Widgets de entrada ---
        self.lbl_nombre = QLabel("Nombre del medicamento:") 
        self.txt_nombre = QLineEdit()

        self.lbl_dosis = QLabel("Dosis:") 
        self.txt_dosis = QLineEdit()  
        self.lbl_hora = QLabel("Hora de toma:")  
        self.time_hora = QTimeEdit() 
        self.time_hora.setDisplayFormat("hh:mm AP") 
        self.time_hora.setTime(QTime.currentTime())  

        # --- Botones ---
        self.btn_agregar = QPushButton("Agregar medicamento")  
        self.btn_eliminar = QPushButton("Eliminar seleccionado") 
        self.btn_limpiar = QPushButton("Limpiar lista")  

        # --- Lista de medicamentos ---
        self.lista_medicamentos = QListWidget() 

        # --- Conectar botones con funciones ---
        self.btn_agregar.clicked.connect(self.agregar_medicamento)
        self.btn_eliminar.clicked.connect(self.eliminar_medicamento)
        self.btn_limpiar.clicked.connect(self.limpiar_lista)

        # --- Layout: organizar widgets en la ventana ---
        layout = QVBoxLayout()

        # Primera fila: nombre
        fila1 = QHBoxLayout()  
        fila1.addWidget(self.lbl_nombre)
        fila1.addWidget(self.txt_nombre)

        # Segunda fila: dosis
        fila2 = QHBoxLayout()
        fila2.addWidget(self.lbl_dosis)
        fila2.addWidget(self.txt_dosis)

        # Tercera fila: hora
        fila3 = QHBoxLayout()
        fila3.addWidget(self.lbl_hora)
        fila3.addWidget(self.time_hora)

        # Añadir filas y botones al layout principal
        layout.addLayout(fila1)
        layout.addLayout(fila2)
        layout.addLayout(fila3)
        layout.addWidget(self.btn_agregar)
        layout.addWidget(self.btn_eliminar)
        layout.addWidget(self.btn_limpiar)
        layout.addWidget(self.lista_medicamentos)

        self.setLayout(layout)  

        # --- Lista interna para almacenar medicamentos ---
        self.medicamentos = [] 

        # --- Timer para notificaciones ---
        self.timer = QTimer()
        self.timer.timeout.connect(self.verificar_medicamentos)
        self.timer.start(60000)  # Verifica cada 60 segundos


    # --- Función para agregar medicamento con validaciones ---
    def agregar_medicamento(self):
        # Obtener datos de los campos de entrada
        nombre = self.txt_nombre.text().strip()
        dosis = self.txt_dosis.text().strip()
        hora = self.time_hora.time().toString("hh:mm AP")

        # Validar que los campos no estén vacíos
        if nombre == "" or dosis == "":
            QMessageBox.warning(self, "Error", "Debe completar todos los campos.")
            return

        # Crear registro 
        registro = f"💊 {nombre} - {dosis} a las {hora}"

        # Evitar mismo medicamento a la misma hora
        if registro in self.medicamentos:
            QMessageBox.warning(self, "Error", "Este medicamento ya está registrado a esa hora.")
            return

        # Agregar a la lista interna y actualizar la lista visual
        self.medicamentos.append(registro)
        self.lista_medicamentos.addItem(registro)

        # Limpiar campos de texto para ingresar nuevo medicamento
        self.txt_nombre.clear()
        self.txt_dosis.clear()

    # --- Función para eliminar medicamento seleccionado ---
    def eliminar_medicamento(self):
        # Obtener el item seleccionado en la lista
        item = self.lista_medicamentos.currentItem()
        if item:
            # Eliminar de la lista interna y visual
            self.medicamentos.remove(item.text())
            self.lista_medicamentos.takeItem(self.lista_medicamentos.row(item))
        else:
            # Mostrar advertencia si no hay selección
            QMessageBox.warning(self, "Error", "Seleccione un medicamento para eliminar.")

    # --- Función para limpiar toda la lista ---
    def limpiar_lista(self):
        self.medicamentos.clear()  
        self.lista_medicamentos.clear() 

 # --- Función para verificar medicamentos a la hora actual ---
    def verificar_medicamentos(self):
        hora_actual = QTime.currentTime().toString("hh:mm AP")
        for med in self.medicamentos:
           if med.endswith(hora_actual):
             QMessageBox.information(self, "Recordatorio", f"Es hora de tomar: {med}")

if __name__ == "__main__":
    app = QApplication(sys.argv)


    ventana = RecordatorioMedicamentos() 
    ventana.show() 
    sys.exit(app.exec_()) 

















