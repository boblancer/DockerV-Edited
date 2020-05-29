import sys
from PySide2 import QtWidgets, QtGui
from PySide2 import QtCore
from PySide2 import QtUiTools
from pyside_material import apply_stylesheet
from clickable import ClickableLabel


class ContainerListItem(QtWidgets.QWidget):
    def __init__(self, c_name, i_name, ip,  owner, ports=[]):
        super(ContainerListItem, self).__init__()
        self.check_box = QtWidgets.QCheckBox()
        self.container_name = ClickableLabel(c_name)
        self.image_name = ClickableLabel(i_name)
        self.ip = QtWidgets.QLabel(ip)
        self.ports = QtWidgets.QPushButton("9000:9000")
        self.ownerships = QtWidgets.QLabel(owner)
        self.set_ui()

    def set_ui(self):
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.check_box)
        layout.addWidget(self.container_name)
        layout.addWidget(self.image_name)
        layout.addWidget(self.ip)
        layout.addWidget(self.ports)
        layout.addWidget(self.ownerships)
        layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.setLayout(layout)
        self.show()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.widget = ContainerListItem("alpine", "q12", "120.10.1.1", "baypc")

        self.setWindowTitle("DockerV")

        self.setCentralWidget(self.widget)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
