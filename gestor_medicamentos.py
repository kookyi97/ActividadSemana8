import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QTimeEdit, QListWidget
)
from PyQt5 import QtGui
from PyQt5.QtCore import QTime

class RecordatorioMedicamentos(QWidget):
    def __init__(self):
        super().__init__()

        # --- Configuración de la ventana ---
        self.setWindowTitle("Recordatorio de Medicamentos")
        self.setGeometry(300, 200, 500, 400)

        # --- Widgets ---
        self.lbl_nombre = QLabel("Nombre del medicamento:")
        self.txt_nombre = QLineEdit()

        self.lbl_dosis = QLabel("Dosis:")
        self.txt_dosis = QLineEdit()

        self.lbl_hora = QLabel("Hora de toma:")
        self.time_hora = QTimeEdit()
        self.time_hora.setDisplayFormat("hh:mm AP")
        self.time_hora.setTime(QTime.currentTime())

        # Botones
        self.btn_agregar = QPushButton("Agregar medicamento")
        self.btn_eliminar = QPushButton("Eliminar seleccionado")
        self.btn_limpiar = QPushButton("Limpiar lista")

        # Lista de medicamentos
        self.lista_medicamentos = QListWidget()

        # --- Conectar botones ---
        self.btn_agregar.clicked.connect(self.agregar_medicamento)
        self.btn_eliminar.clicked.connect(self.eliminar_medicamento)
        self.btn_limpiar.clicked.connect(self.limpiar_lista)

        # --- Layouts ---
        layout = QVBoxLayout()

        fila1 = QHBoxLayout()
        fila1.addWidget(self.lbl_nombre)
        fila1.addWidget(self.txt_nombre)

        fila2 = QHBoxLayout()
        fila2.addWidget(self.lbl_dosis)
        fila2.addWidget(self.txt_dosis)

        fila3 = QHBoxLayout()
        fila3.addWidget(self.lbl_hora)
        fila3.addWidget(self.time_hora)

        layout.addLayout(fila1)
        layout.addLayout(fila2)
        layout.addLayout(fila3)
        layout.addWidget(self.btn_agregar)
        layout.addWidget(self.btn_eliminar)
        layout.addWidget(self.btn_limpiar)
        layout.addWidget(self.lista_medicamentos)

        self.setLayout(layout)

        # --- Lista interna ---
        self.medicamentos = []

    # --- Función para agregar medicamento ---
    def agregar_medicamento(self):
        nombre = self.txt_nombre.text().strip()
        dosis = self.txt_dosis.text().strip()
        hora = self.time_hora.time().toString("hh:mm AP")

        if nombre == "" or dosis == "":
            QMessageBox.warning(self, "Error", "Debe completar todos los campos.")
            return

        registro = f"💊 {nombre} - {dosis} a las {hora}"

        # Evitar duplicados
        if registro in self.medicamentos:
            QMessageBox.warning(self, "Error", "Este medicamento ya está registrado a esa hora.")
            return

        # Guardar y actualizar lista
        self.medicamentos.append(registro)
        self.lista_medicamentos.addItem(registro)

        # Limpiar campos de texto
        self.txt_nombre.clear()
        self.txt_dosis.clear()

    # --- Función para eliminar medicamento seleccionado ---
    def eliminar_medicamento(self):
        item = self.lista_medicamentos.currentItem()
        if item:
            self.medicamentos.remove(item.text())
            self.lista_medicamentos.takeItem(self.lista_medicamentos.row(item))
        else:
            QMessageBox.warning(self, "Error", "Seleccione un medicamento para eliminar.")

    # --- Función para limpiar toda la lista ---
    def limpiar_lista(self):
        self.medicamentos.clear()
        self.lista_medicamentos.clear()

# --- Programa principal ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QtGui.QFont("Verdana", 10))

    ventana = RecordatorioMedicamentos()
    ventana.show()
    sys.exit(app.exec_())
