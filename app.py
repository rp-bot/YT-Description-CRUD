import sys
from PyQt5.QtWidgets import QApplication
from mainGUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import urllib.request
from read_only import get_video_details


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        self.link_input_box.returnPressed.connect(self.handleReturnPressed)

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
