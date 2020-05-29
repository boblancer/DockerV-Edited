from PySide2 import QtWidgets, QtGui
import sys
from ContainerListItem import Container


class CustomListHead(QtWidgets.QWidget):
    def __init__(self):
        super(CustomListHead, self).__init__()
        self.project_title = QtWidgets.QLabel("Today")
        self.set_ui()

    def set_ui(self):
        grid_box = QtWidgets.QGridLayout()
        grid_box.addWidget(self.project_title, 0, 0)

        self.setLayout(grid_box)
        self.show()


class CustomListItem(QtWidgets.QWidget):
    def __init__(self):
        super(CustomListItem, self).__init__()
        self.project_title = QtWidgets.QLabel("Learn Python")
        self.task_title = QtWidgets.QLabel(
            "Learn more about forms, models and include")
        self.con = Container()
        self.set_ui()

    def set_ui(self):
        grid_box = QtWidgets.QGridLayout()
        grid_box.addWidget(self.project_title, 0, 0)
        grid_box.addWidget(self.task_title, 1, 0)
        grid_box.addWidget(self.con)

        self.setLayout(grid_box)
        self.show()


class MainWindowUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.list_widget = QtWidgets.QListWidget()
        self.set_ui()

    def set_ui(self):
        custom_head_item = CustomListHead()

        item = QtWidgets.QListWidgetItem(self.list_widget)
        item.setSizeHint(custom_head_item.sizeHint())

        self.list_widget.setItemWidget(item, custom_head_item)
        self.list_widget.addItem(item)

        custom_item = CustomListItem()
        item = QtWidgets.QListWidgetItem(self.list_widget)
        item.setSizeHint(custom_item.sizeHint())

        self.list_widget.addItem(item)
        self.list_widget.setItemWidget(item, custom_item)

        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.addWidget(self.list_widget)

        widget = QtWidgets.QWidget()
        widget.setLayout(vertical_layout)
        self.setCentralWidget(widget)
        self.show()


app = QtWidgets.QApplication(sys.argv)
ui = MainWindowUI()
sys.exit(app.exec_())
