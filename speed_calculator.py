from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
QLineEdit, QPushButton, QComboBox
import sys
from datetime import datetime


# Method 1 age_calculator = QWidget()

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours): ")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")


        # Add widgets togrid
        grid.addWidget(distance_label, 0,0)
        grid.addWidget(self.distance_line_edit, 0,1)
        grid.addWidget(time_label, 1,0)
        grid.addWidget(self.time_line_edit, 1,1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)


        # Adding Units 
        ...
        self.unitsChoice = QComboBox()
        self.unitsChoice.addItems(['Imperial (miles)', 'Metric (km)'])
        grid.addWidget(self.unitsChoice, 0,3)

        ...

    def calculate_speed(self):
        speed = float(self.distance_line_edit.text()) / float(self.time_line_edit.text())
        if self.unitsChoice.currentText() == 'Imperial (miles)':
            unit = "mph"
        if self.unitsChoice.currentText() == 'Metric (km)':
            unit = "km/h"
        self.output_label.setText(f"Average Speed: {speed:.3f} {unit}")



app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())