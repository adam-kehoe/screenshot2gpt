import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRubberBand
from PyQt5.QtCore import Qt, QPoint, QRect, QSize
from PyQt5.QtGui import QScreen, QPainter, QColor
from PyQt5.QtCore import QTimer
from dialog import APIDataDialog
from vision import analyze_image
from prompts import Prompts

prompts = Prompts()
ANALYSIS_MODE = prompts.uiux

class ScreenCaptureTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.origin = QPoint()
        self.selectionRect = QRect()
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.isSelecting = False

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showMaximized()

    def mousePressEvent(self, event):
        self.origin = event.globalPos()
        self.selectionRect = QRect(self.origin, QSize())
        self.rubberBand.setGeometry(self.selectionRect)
        self.rubberBand.show()
        self.isSelecting = True

    def mouseMoveEvent(self, event):
        if self.isSelecting:
            self.selectionRect = QRect(self.origin, event.globalPos()).normalized()
            self.rubberBand.setGeometry(self.selectionRect)
            self.update()

    def mouseReleaseEvent(self, event):
        if self.isSelecting:
            self.isSelecting = False
            self.rubberBand.hide()
            self.selectionRect = self.rubberBand.geometry()
            self.hide()  # Hide the overlay window before taking the screenshot
            # N.B. this may not be necessary; hacking around to fix a bug
            QTimer.singleShot(
                200, self.captureScreen
            )  # Delay the capture to ensure the window is hidden

    def captureScreen(self):
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(
            0,
            self.selectionRect.x(),
            self.selectionRect.y(),
            self.selectionRect.width(),
            self.selectionRect.height(),
        )

        screenshot.save("screenshot.png", "png")
        analysis = analyze_image("screenshot.png", ANALYSIS_MODE)
        self.dialog = APIDataDialog()
        self.dialog.setText(analysis)
        self.dialog.show()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 100))  # Dark overlay
        if self.isSelecting:
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.fillRect(self.selectionRect, Qt.transparent)


def main():
    app = QApplication(sys.argv)
    ex = ScreenCaptureTool()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
