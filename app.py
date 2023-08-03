import sys
from PyQt5.QtWidgets import QApplication
from mainGUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem,QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import urllib.request

from read_only import get_video_details
from GPT import get_response_from_ChatGPT

from time import sleep


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        self.link_input_box.returnPressed.connect(self.handleReturnPressed)
        self.ask_btn.clicked.connect(self.handleAskButtonClicked)

    def handleAskButtonClicked(self):
        # Get the text from the QTextEdit

        # Get the text from the QTextEdit
        text = self.ask_chatgpt.toPlainText()
        QApplication.setOverrideCursor(Qt.WaitCursor)
        # Process the text with a delay to simulate a long-running operation
        gpt_response = get_response_from_ChatGPT(text)
        QApplication.restoreOverrideCursor()
        # gpt_response = get_response_from_ChatGPT(text)
        # result = process_text(text)

        self.gpt_response.setText(gpt_response)

    def handleReturnPressed(self):
        link = self.link_input_box.text()

    # Parse the video ID from the URL
        video_id = link.split("v=")[1]

        title, description, thumb_url = get_video_details(video_id)
        self.videotitle.setText(title)
        self.read_video_desc.setText(description)

        # Download the thumbnail image
        data = urllib.request.urlopen(thumb_url).read()

        # Create a QPixmap from the downloaded data
        pixmap = QPixmap()
        pixmap.loadFromData(data)

        # Create a QGraphicsPixmapItem to display the QPixmap in the QGraphicsView
        item = QGraphicsPixmapItem(pixmap)

        # Clear the QGraphicsView and display the new QGraphicsPixmapItem
        self.thumb.setScene(QGraphicsScene())
        self.thumb.scene().addItem(item)
        self.thumb.fitInView(item, Qt.KeepAspectRatio)

        # Request video details from the YouTube API


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
