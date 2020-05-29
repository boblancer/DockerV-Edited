from pyside_material import apply_stylesheet
from PySide2 import QtWidgets, QtGui, QtCore
from ListItem import ContainerListItem
from Connection import Connection
import sys


class CustomListHead(QtWidgets.QWidget):
    def __init__(self):
        super(CustomListHead, self).__init__()
        self.project_title = QtWidgets.QLabel("Today")
        self.set_ui()

    def set_ui(self):
        self.show()


# -----------------------------------
class ListWidget(QtWidgets.QListWidget):
    def __init__(self):
        super(ListWidget, self).__init__()
        self.ListHead = CustomListHead()
        self.ListItems = []
        self.set_ui()

    def set_ui(self):
        self.update(self.ListHead)
        pass

    def UpdateList(self, containers):
        for c in containers:
            ListItem = ContainerListItem(
                c.image.short_id, c.name, "127.0.0.1", "bay pc")
            print(c.attrs)
            self.addCustomItem(ListItem)

    def addCustomItem(self, widget):
        self.ListItems.append(widget)
        self.update(widget)

    def update(self, widget):
        item = QtWidgets.QListWidgetItem(self)
        item.setFlags(QtCore.Qt.NoItemFlags)
        item.setSizeHint(QtCore.QSize(40, 80))
        self.addItem(item)
        self.setItemWidget(item, widget)


class MainWindowUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.list_widget = ListWidget()
        self.set_ui()

    def set_ui(self):
        c = Connection()
        lst = c.getContainersDetail()
        self.list_widget.UpdateList(lst)
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.addWidget(self.list_widget)
        apply_stylesheet(app, theme='dark_teal.xml')
        widget = QtWidgets.QWidget()
        widget.setLayout(vertical_layout)
        self.setCentralWidget(widget)
        self.show()


app = QtWidgets.QApplication(sys.argv)
ui = MainWindowUI()
sys.exit(app.exec_())
