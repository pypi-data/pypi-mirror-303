import os
import os.path as opath
import qwork.icon_rc
from qwork.qtimp import *
from qwork.qtclrs import LT_YELLOW


def get_icon_from_path(path):
    base_dir, fnametype = opath.split(path)
    fname, ftype = opath.splitext(fnametype)
    icon = QIcon()
    if opath.isdir(path):
        if path.lower().endswith(".ipc"):
            icon.addPixmap(QPixmap(":/ficon/ipc.png"), QIcon.Normal, QIcon.Off)
        else:
            icon.addPixmap(QPixmap(":/ficon/dir.png"), QIcon.Normal, QIcon.Off)
    else:
        ftype = ftype.lower()
        if ftype.startswith("."):
            ftype = ftype[1:]
        if ftype == "ipc":
            icon.addPixmap(QPixmap(":/ficon/ipc.png"), QIcon.Normal, QIcon.Off)
        elif ftype in ["v", 'sv']:
            icon.addPixmap(QPixmap(":/ficon/codev.png"), QIcon.Normal, QIcon.Off)
        elif ftype in ['doc', 'docx']:
            icon.addPixmap(QPixmap(":/ficon/word.png"), QIcon.Normal, QIcon.Off)
        elif ftype in ['xls', 'xlsx']:
            icon.addPixmap(QPixmap(":/ficon/excel.png"), QIcon.Normal, QIcon.Off)
        elif ftype in ['ppt', 'pptx']:
            icon.addPixmap(QPixmap(":/ficon/ppt.png"), QIcon.Normal, QIcon.Off)
        elif ftype == "pdf":
            icon.addPixmap(QPixmap(":/ficon/pdf.png"), QIcon.Normal, QIcon.Off)
        elif ftype in ['py', 'c', 'h', 'cpp', 'hpp', 'cs', 'js']:
            icon.addPixmap(QPixmap(":/ficon/code.png"), QIcon.Normal, QIcon.Off)
        elif ftype in ['png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff']:
            icon.addPixmap(QPixmap(":/ficon/image.png"), QIcon.Normal, QIcon.Off)
        elif ftype in ["zip", 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'zst', 'lzma', 'lz4']:
            icon.addPixmap(QPixmap(":/ficon/zip.png"), QIcon.Normal, QIcon.Off)
        elif ftype == "exe":
            icon.addPixmap(QPixmap(":/ficon/exe.png"), QIcon.Normal, QIcon.Off)
        elif ftype == "txt":
            icon.addPixmap(QPixmap(":/ficon/txt.png"), QIcon.Normal, QIcon.Off)
        else:
            icon.addPixmap(QPixmap(":/ficon/file.png"), QIcon.Normal, QIcon.Off)
    return icon

class QFixWidthLabel(QLabel):
    FONT = None
    METRICS = None
    LINESPACE = None
    SINGLINEH = None
    SINGLABELH = None


    @classmethod
    def __initial__(cls):
        cls.FONT = QFont("Arial", 10, QFont.Normal)
        cls.METRICS = QFontMetrics(cls.FONT)
        cls.LINESPACE = 2
        cls.SINGLINEH = cls.METRICS.height()
        cls.SINGLABELH = cls.SINGLINEH + cls.LINESPACE * 2

    def __init__(self, fixed_width: int, parent=None):
        """

        :param fixed_width:     固定宽度
        :param parent:        父窗口, 默认为None
        :param linespace:   行间距, 默认为2
        """
        if self.FONT is None:
            self.__initial__()
        assert parent is None or isinstance(parent, QWidget), "parent must be a QWidget or None."
        super(QFixWidthLabel, self).__init__(parent)
        super(QFixWidthLabel, self).setFont(self.FONT)
        super(QFixWidthLabel, self).setFixedWidth(fixed_width)
        super(QFixWidthLabel, self).setMinimumHeight(self.SINGLABELH)
        self._cur_lines = 1  # current lines
        self._max_lines = 9999  # max lines


    def setMinimumHeight(self, a0):
        raise NotImplementedError("QFixWidthLabel: setMinimumHeight is not allowed.")

    def setMaximumHeight(self, a0):
        raise NotImplementedError("QFixWidthLabel: setMaximumHeight is not allowed.")

    def setFixedHeight(self, a0):
        raise NotImplementedError("QFixWidthLabel: setFixedHeight is not allowed.")

    def setFixedWidth(self, a0):
        raise NotImplementedError("QFixWidthLabel: setFixedWidth is not allowed.")

    def setFont(self, a0):
        raise NotImplementedError("QFixWidthLabel: setFont is not allowed.")


    @classmethod
    def GetHeight(cls, lines: int):
        if cls.FONT is None:
            cls.__initial__()
        assert lines > 0, "lines must be greater than 0."
        return lines * cls.SINGLINEH + (lines + 1) * cls.LINESPACE

    def height(self):
        return self.GetHeight(self._cur_lines)

    def maximumHeight(self):
        return self.GetHeight(self._max_lines)

    def currentLines(self) -> int:
        return self._cur_lines

    def maxLines(self) -> int:
        return self._max_lines


    def setMaxLines(self, max_lines: int):
        """
        设置最大行数

        * 对于N行文本, 最大高度 N * _SINGLINEH + (N + 1) * _linespace

        :param max_lines:
        :return:
        """
        self._max_lines = max_lines
        super().setMaximumHeight(self.GetHeight(max_lines))
        if self._cur_lines > self._max_lines:
            self.setText(self.text())

    @property
    def h(self) -> int:
        return self.height()

    @property
    def maxh(self) -> int:
        return self.maximumHeight()

    @property
    def lines(self) -> int:
        return self.currentLines()

    @property
    def maxlines(self) -> int:
        return self.maxLines()

    @maxlines.setter
    def maxLines(self, max_lines: int):
        self.setMaxLines(max_lines)

    def setText(self, text):
        lines = []
        current = ""
        width = self.width()

        for char in text:
            current += char
            if self.METRICS.width(current) > width:
                lines.append(current[:-1])
                current = char
        lines.append(current)

        self._cur_lines = len(lines)
        super().setText("\n".join(lines))


class QFileItem(QWidget):
    dragAccepted = pyqtSignal()
    dragIgnored = pyqtSignal()
    dragPicked = pyqtSignal()

    MODE_MOVE = 'mov'
    MODE_COPY = 'cpy'

    def __init__(self, filepath=None, parent=None, *, size=64, dragmode=MODE_MOVE):
        super().__init__(parent)
        self._filepath = opath.abspath(filepath) if filepath is not None else None
        self._icon = get_icon_from_path(filepath) if filepath is not None else QIcon()
        self._dragmode = dragmode
        self._size = size
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(1)
        self.setLayout(self.layout)

        # icon
        self.icon_lbl = QLabel()
        self.icon_lbl.setPixmap(self._icon.pixmap(self._size, self._size))
        self.icon_lbl.setFixedSize(self._size, self._size)
        self.layout.addWidget(self.icon_lbl)

        # name
        self.name_lbl = QFixWidthLabel(self._size)
        self.name_lbl.setText(self.basename)
        self.name_lbl.setMaxLines(3)
        self.name_lbl.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.layout.addWidget(self.name_lbl)

        # size cst
        self.setFixedWidth(self._size)
        self.setMinimumHeight(self.height())
        self.setMaximumHeight(self.maxiumHeight())


    @property
    def basename(self):
        if self._filepath is None:
            return ""
        return opath.basename(self._filepath)

    @property
    def dirname(self):
        if self._filepath is None:
            return ""
        return opath.dirname(self._filepath)

    @property
    def fname(self):
        if self._filepath is None:
            return ""
        if self.isdir:
            return self.basename
        else:
            return opath.splitext(self.basename)[0]

    @property
    def ftype(self):
        if self._filepath is None:
            return ""
        if self.isdir:
            return "dir"
        else:
            return opath.splitext(self._filepath)[1]

    @property
    def path(self):
        if self._filepath is None:
            return ""
        return self._filepath

    @path.setter
    def path(self, value):
        if not opath.exists(value):
            raise FileNotFoundError(f"File not found: {value}")
        self._filepath = os.path.abspath(value)
        self._icon = get_icon_from_path(value)
        self.icon_lbl.setPixmap(self._icon.pixmap(self._size, self._size))
        self.name_lbl.setText(self.basename)
        self.setMinimumHeight(self.height())
        self.setMaximumHeight(self.maxiumHeight())

    @property
    def isdir(self) -> bool:
        if self._filepath is None:
            return False
        return opath.isdir(self._filepath)

    @property
    def isfile(self) -> bool:
        if self._filepath is None:
            return False
        return opath.isfile(self._filepath)

    @property
    def exists(self) -> bool:
        if self._filepath is None:
            return False
        return opath.exists(self._filepath)



    def width(self):
        return self._size

    def height(self):
        return self._size + self.name_lbl.height() + 1

    def maxiumHeight(self):
        return self._size + self.name_lbl.maximumHeight() + 1

    def setPath(self, path):
        self.path = path

    # 双击检测
    def mouseDoubleClickEvent(self, event):
        # os
        os.startfile(self._filepath)

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return

        if self._filepath is None:
            return

        # 开始拖拽操作
        drag = QDrag(self)
        mimeData = QMimeData()
        mimeData.setText(self.path)
        mimeData.setUrls([QUrl.fromLocalFile(self.path)])
        drag.setMimeData(mimeData)
        drag.setPixmap(self._icon.pixmap(self._size // 2, self._size // 2))
        self.setVisible(False)
        self.dragPicked.emit()

        # 执行拖拽
        drop_action = drag.exec_(Qt.MoveAction if self._dragmode == self.MODE_MOVE else
                                 Qt.CopyAction if self._dragmode == self.MODE_COPY else Qt.IgnoreAction)

        # 根据拖拽结果更新状态
        if drop_action == Qt.IgnoreAction:
            self.dragIgnored.emit()
            self.setVisible(True)
        else:
            self.dragAccepted.emit()
            if self._dragmode == self.MODE_MOVE:
                self.deleteLater()


class QFilesView(QWidget):
    def __init__(self, parent=None):
        super(QFilesView, self).__init__(parent)
        self._paths = []  # 用于存储文件路径的列表
        self.initUI()

    def initUI(self):
        # 设置布局
        self.layout = QVBoxLayout(self)

        # 设置滚动区域
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget(self.scroll_area)
        self.scroll_layout = QGridLayout(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout.addWidget(self.scroll_area)

        # 启用拖拽事件
        self.setAcceptDrops(True)

    def clear(self):
        self._paths = []
        self.update_after()

    @property
    def paths(self):
        return self._paths

    @paths.setter
    def paths(self, paths):
        self._paths = paths
        self.update_after()

    @property
    def files(self) -> str:
        res = []
        for path in self._paths:
            if os.path.isfile(path):
                res.append(path)
            else:
                for root, _, files in os.walk(path):
                    for f in files:
                        _path = os.path.join(root, f)
                        if os.path.isfile(_path):
                            res.append(_path)
        return res

    def mouseDoubleClickEvent(self, a0):
        paths, _ = QFileDialog.getOpenFileNames(self, "Open Files", "", "All Files(*)")

        if paths:
            self._paths = paths
            self._sort_paths()
            self.update_after()

    def update_after(self):
        # 清除当前的布局
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            self.scroll_layout.removeWidget(widget)
            widget.deleteLater()

        # 绘制文件图标和文件名
        width = self.scroll_widget.width()
        cnt = width // (64 + 8)
        length = len(self._paths)
        rows = length // cnt + 1
        # for i, path in enumerate(self._paths):
        #     icon_label = FileIconLabel(path, self.scroll_widget)
        #     self.scroll_layout.addWidget(icon_label, i // cnt, i % cnt, Qt.AlignLeft)
        for ih in range(rows):
            for iw in range(cnt):
                idx = ih * cnt + iw
                if idx >= length:
                    # self.scroll_layout.setRowStretch(ih, 1)
                    break
                path = self._paths[idx]
                icon_label = QFileItem(path, self.scroll_widget, size=64)
                self.scroll_layout.addWidget(icon_label, ih, iw, Qt.AlignLeft)
            # add stregth
        self.scroll_layout.setRowStretch(999, 1)
        self.scroll_layout.setColumnStretch(999, 1)

        self.scroll_widget.adjustSize()

    def dragEnterEvent(self, event: QDragEnterEvent):
        # 如果事件包含 URL，我们允许它进入
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def _sort_paths(self):
        """
        按照dir在前，file在后的顺序排序
        """
        dirs = []
        files = []
        for path in self._paths:
            if os.path.isdir(path):
                dirs.append(path)
            else:
                files.append(path)
        dirs.sort()
        files.sort()
        self._paths = dirs + files

    def dropEvent(self, event: QDropEvent):
        # 获取拖拽的文件
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        _new = self._paths + files
        self._paths = list(set(_new))  # 去重
        self._sort_paths()
        self.update_after()  # 调用更新方法

    def add_path(self, path):
        self._paths.append(path)
        self.update_after()


class QFileSlot(QWidget):
    fileChanged = pyqtSignal(str)  # 文件路径发生变化时发射的信号, 空文件时发射空字符串

    def __init__(self, parent=None, *, size=64, dragcut=True, formats=None):
        super(QFileSlot, self).__init__(parent)
        self._dragcut = dragcut
        self._size = size
        self._formats = None
        self._bdcolor = LT_YELLOW
        self._bdwidth = 1
        self.formats = formats
        self.initUI()
        self.setAcceptDrops(True)

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 2)
        self.layout.setSpacing(0)

        self.file_item = None
        # self.layout.addWidget(self.file_item)

        self.setFixedWidth(self._size)
        self.reheight()

    def reheight(self, font=None):
        font = font or self.font()
        self.setMinimumHeight(self._size + 4 + QFixWidthLabel.GetHeight(1))
        self.setMaximumHeight(self._size + 4 + QFixWidthLabel.GetHeight(3))

    @property
    def filetype(self):
        if self.file_item is None:
            return ""
        return self.file_item.ftype

    # 双击检测，弹出文件打开对话框
    def mouseDoubleClickEvent(self, event):
        # calc "All Files(*);;Text Files(*.txt)"
        if self._formats is None or len(self._formats) == 0:
            typehints = "All Files(*)"
        else:
            if len(self._formats) == 1:
                typehints = f"{self._formats[0].upper()} Files("
            elif 1 < len(self._formats) < 4:
                _ = [f.upper() for f in self._formats]
                typehints = f"{' '.join(_)} Files("
            else:
                _ = [f.upper() for f in self._formats]
                typehints = f"{' '.join(_[:3]) + '...'} Files("

            for fmt in self._formats:
                typehints += f"*.{fmt} "
            typehints += ")"

        # QFileDialog
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", typehints)

        if path:
            self.setPath(path)

    # 右键单击，移除文件(path=None)
    def mouseReleaseEvent(self, a0):
        if a0.button() == Qt.RightButton:
            self.setPath(None)

    @property
    def path(self) -> str:
        if self.file_item is None:
            return ""
        return self.file_item.path

    @path.setter
    def path(self, path):
        self.setPath(path)

    @property
    def formats(self):
        return self._formats

    @formats.setter
    def formats(self, fmts):
        if fmts is not None:
            # remove '.' if exists
            fmts = [f[1:] if f.startswith(".") else f for f in fmts]
        self._formats = fmts

    def setPath(self, path=None) -> None:
        if path is None or path == "":
            if self.file_item is not None:
                self.file_item.deleteLater()
                self.file_item = None
                self.reheight()
                self.fileChanged.emit("")
            return

        # check file format
        if self._formats is not None:
            suffix = opath.splitext(path)[1][1:]
            if suffix not in self._formats:
                QMessageBox.warning(self, "Warning", f"Only support {self._formats} file format.")
                return

        if self.file_item is None:
            self.file_item = QFileItem(path, self, size=self._size)
            self.layout.addWidget(self.file_item)
            self.file_item.dragAccepted.connect(self.on_accepted)
        self.file_item.path = path
        self.fileChanged.emit(path)
        self.setFixedHeight(self.file_item.height())

    def on_accepted(self):
        if self._dragcut:
            self.file_item.deleteLater()
            self.file_item = None

    # .border(1, Qt.SolidLine, QColor(225, 25, 25, 200))
    def setBorder(self, width: int, color: QColor):
        self._bdwidth = width
        self._bdcolor = color
        if width > 4:
            raise ValueError("QFileSlot:Border width should be less than 4 as Expected.")

    def border(self) -> tuple:
        return self._bdwidth, self._bdcolor

    def paintEvent(self, a0):
        # draw rect
        painter = QPainter(self)
        painter.setPen(QPen(self._bdcolor, self._bdwidth, Qt.SolidLine if self.file_item is not None else Qt.DashLine))

        # painter.drawRect(0, 0, self.width() - 1, self.height() - 1)  # need adjust
        painter.drawRect(int(self._bdwidth / 2), int(self._bdwidth / 2), self.width() - self._bdwidth, self.height() - self._bdwidth)

        super(QFileSlot, self).paintEvent(a0)

    def dragEnterEvent(self, event: QDropEvent):
        mime = event.mimeData()
        if not mime.hasUrls():
            event.ignore()
            return
        if self._formats is None:
            event.accept()
        else:
            tarpaths = [u.toLocalFile() for u in mime.urls()]
            for path in tarpaths:
                suffix = opath.splitext(path)[1][1:]
                if suffix not in self._formats:
                    event.ignore()
                    return
            event.accept()

    def dropEvent(self, event: QDropEvent):
        # 获取拖拽的文件
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files:
            self.setPath(files[0])
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication([])
    w = QWidget()
    fs = QFileItem()
    fs.setPath("3dobj.png")
    w.setLayout(QHBoxLayout())
    w.layout().addWidget(fs)
    w.layout().addWidget(QFileSlot())
    w.show()
    app.exec_()





