import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class APIDataDialog(QDialog):
    def __init__(self, parent=None):
        super(APIDataDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('GPT Response')
        self.setGeometry(100, 100, 600, 400)  # Adjust size as needed
        layout = QVBoxLayout()

        # Main text area
        self.main_text_edit = QTextEdit(self)
        self.main_text_edit.setPlaceholderText("API Response will be shown here...")
        self.main_text_edit.setReadOnly(True)  # If you want to prevent user from editing the text
        self.main_text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Close button
        self.close_button = QPushButton('Close', self)
        self.close_button.clicked.connect(self.close)

        # Add widgets to the layout
        layout.addWidget(self.main_text_edit)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def setText(self, text):
        self.main_text_edit.setText(text)

