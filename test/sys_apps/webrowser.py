import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebBrowser(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simple Web Browser')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.url_entry = QLineEdit()
        layout.addWidget(self.url_entry)

        self.open_button = QPushButton('Ouvrir')
        self.open_button.clicked.connect(self.open_url)
        layout.addWidget(self.open_button)

        self.webview = QWebEngineView()
        layout.addWidget(self.webview)

        self.setLayout(layout)

    def open_url(self):
        url = self.url_entry.text()
        if url.strip() != "":
            self.webview.load(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
