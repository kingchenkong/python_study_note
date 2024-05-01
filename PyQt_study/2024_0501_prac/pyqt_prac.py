import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def say_hello():
    print("Hello World")


if __name__ == '__main__':
    # 建立應用程式物件
    app = QApplication(sys.argv)

    # 建立主視窗物件
    window = QWidget()
    window.setWindowTitle('Hellooo~~ world!!')
    window.setGeometry(100, 100, 400, 300)  # 設定視窗位置與大小

    # 新增按鈕
    button = QPushButton('say Hello~', window)
    button.setGeometry(150, 150, 100, 30)  # 設定按鈕位置和大小

    # 將按鈕點擊事件與函式連接
    button.clicked.connect(say_hello)

    # 顯示視窗
    window.show()

    # 執行應用程式的訊息迴圈
    sys.exit(app.exec_())
