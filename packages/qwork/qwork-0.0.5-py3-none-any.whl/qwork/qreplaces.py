from qwork.qtimp import QTextEdit, pyqtSignal

class QTextEdit(QTextEdit):
    getFocus = pyqtSignal()
    lostFocus = pyqtSignal()

    def focusInEvent(self, a0):
        self.getFocus.emit()
        super(QTextEdit, self).focusInEvent(a0)

    def focusOutEvent(self, a0):
        self.lostFocus.emit()
        super(QTextEdit, self).focusOutEvent(a0)




