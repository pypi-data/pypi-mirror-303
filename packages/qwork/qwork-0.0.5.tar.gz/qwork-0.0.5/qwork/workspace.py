from qwork.utils import *
from PyQt5.QtWidgets import QBoxLayout

class QWidgetArea(QWidget):
    def __init__(self, parent=None):
        super(QWidgetArea, self).__init__(parent)
        self._layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        super().setLayout(self._layout)
        self._widgets = []  # all widgets in this area

        self._mmf = False   # mouse middle button flag
        self._mmp = None    # mouse middle button press point


    def setLayout(self, a0):
        raise TypeError("QWidgetArea.setLayout() is not supported")

    def layout(self):
        raise TypeError("QWidgetArea.layout() is not supported")

    def mouseMoveEvent(self, a0):
        # move all widgets
        if self._mmf:
            _pos = a0.pos()
            _delta = _pos - self._mmp
            for i, w in enumerate(self._widgets):
                w.move(w.pos() + _delta)
            self._mmp = _pos
        else:
            super(QWidgetArea, self).mouseMove

    def mousePressEvent(self, a0):
        _btn = a0.button()
        if _btn == Qt.MiddleButton:
            self._mmf = True
            self._mmp = a0.pos()
        else:
            super(QWidgetArea, self).mousePressEvent(a0)

    def mouseReleaseEvent(self, a0):
        _btn = a0.button()
        if _btn == Qt.MiddleButton:
            self._mmf = False
            self._mmp = None
        else:
            super(QWidgetArea, self).mouseReleaseEvent(a0)

    def wheelEvent(self, a0):
        _delta = a0.angleDelta().y()
        for i, w in enumerate(self._widgets):
            w.resize(w.width() + _delta, w.height() + _delta)

    def addWidget(self, w):
        self._layout.addWidget(w)
        self._widgets.append(w)


if __name__ == '__main__':
    app = QApplication([])
    w = QWidgetArea()

    w.resize(800, 600)
    lbl = QLabel("Hello, World!")
    lbl.setMaximumSize(200, 200)
    # 显示边框
    lbl.setStyleSheet("border: 1px solid black;")
    w.addWidget(lbl)
    w.show()
    app.exec_()

