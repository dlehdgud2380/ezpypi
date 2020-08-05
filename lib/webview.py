# webview for description.html for only ez_pypi

import os

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class Form(QWidget):
    def __init__(self, title):
        self.title = title
        QWidget.__init__(self, flags=Qt.Widget)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle(self.title)
        web = QWebEngineView()
        url = QUrl.fromLocalFile(r'%s/description.html' % os.getcwd())
        web.load(url)
        self.form_layout.addWidget(web)