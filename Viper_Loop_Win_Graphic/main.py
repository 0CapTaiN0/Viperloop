import subprocess
import sys
import webbrowser
import psutil

from PyQt5.QtGui import QIcon, QPixmap, QFontDatabase, QFont, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QComboBox, QLabel, QDialog, QVBoxLayout, \
 QProgressBar
from PyQt5.QtCore import pyqtSlot, QTimer, Qt



# Find interface
def find_active_network_cards():

    active_interfaces = []

    #Get all interfaces
    network_interfaces = psutil.net_if_stats()

    for interface, stats in network_interfaces.items():
        # Checking the activation of the network card
        if stats.isup:
            active_interfaces.append(interface)

    return active_interfaces


active_cards = find_active_network_cards()







class App(QWidget):
    def __init__(self):
        super().__init__()
        QFontDatabase.addApplicationFont("Font/Roboto-Regular.ttf")
        self.selected_network_card = None
        self.title = 'Viper Loop'
        self.setFont(QFont("Roboto", 5))
        self.combo1 = None
        self.is_progress_bar_active = False

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(290, 490)
        self.setStyleSheet("background-color: #202020")



        # logo
        label_pic = QLabel(self)
        label_pic.setGeometry(83, 2, 160, 160)
        pixmap = QPixmap('icon/logon.png')
        label_pic.setPixmap(pixmap)
        icon = QIcon(QPixmap('icon/logon.png'))
        self.setWindowIcon(icon)



        # panel1
        rect = QFrame(self)
        rect.setGeometry(65, 165, 160, 280)
        rect.setStyleSheet("background-color: #3d3d3d; border-radius : 12px;")



        # panel3
        rect = QFrame(self)
        rect.setGeometry(245, 220, 70, 175)
        rect.setStyleSheet("background-color: #3d3d3d; border-radius : 9px;")


        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(0, 0, 320, 10)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.hide()
        self.progress_bar.setStyleSheet("QProgressBar { color: red; } QProgressBar::chunk { background-color: #72C3FF; }")
        self.progress_bar.setTextVisible(False)


        # ver_label
        ver_label = QLabel('2.1v', self)
        ver_label.move(2, 473)
        ver_label.setStyleSheet('background-color:transparent ;color: white ; font-size: 10px')

        # Select_DNS_label
        select_dns_label = QLabel('Select DNS', self)
        select_dns_label.move(110, 180)
        select_dns_label.setStyleSheet('background-color:#3d3d3d;color: white ; font-size: 13px')

        # Select_NetworkCard_label
        select_networkCard_label = QLabel('Select NetworkCard', self)
        select_networkCard_label.move(87, 240)
        select_networkCard_label.setStyleSheet('background-color:#3d3d3d;color: white ; font-size: 13px')



        # dynamic text(Apply,done)
        self.dynamic_text = QLabel('               ', self)
        self.dynamic_text.move(115, 295)
        self.dynamic_text.setBackgroundRole(QPalette.Base)
        self.dynamic_text.setStyleSheet('background-color:#3d3d3d;color: white ')





        # reset_dns_button
        self.reset_dns_button = QPushButton('Reset DNS', self)
        self.reset_dns_button.move(90, 380)
        self.reset_dns_button.resize(110, 40)


        # set_dns_button
        self.set_dns_button = QPushButton('Set DNS', self)
        self.set_dns_button.resize(self.reset_dns_button.size())
        self.set_dns_button.move(self.reset_dns_button.x(), self.reset_dns_button.y() - 50)


        # download_button
        self.download_button = QPushButton('', self)
        self.download_button.move(250, 310)
        self.download_button.resize(35, 35)
        self.download_button.setStyleSheet("background-color: #3d3d3d; color: #000000; border-radius : 5px;")
        icon = QIcon(QPixmap('icon/download.png'))
        self.download_button.setIcon(icon)
        self.download_button.setIconSize(self.download_button.size())

        # Support_button
        self.support_button = QPushButton('', self)
        self.support_button.move(250, 270)
        self.support_button.resize(35, 35)
        self.support_button.setStyleSheet("background-color: #3d3d3d; color: #000000; border-radius : 5px;")
        icon = QIcon(QPixmap('icon/heart.png'))
        self.support_button.setIcon(icon)
        self.support_button.setIconSize(self.download_button.size())

        # about_me_button
        self.about_me_button = QPushButton('', self)
        self.about_me_button.move(250, 230)
        self.about_me_button.resize(35, 35)
        self.about_me_button.setStyleSheet("background-color: #3d3d3d; color: #000000; border-radius : 5px;")
        icon = QIcon(QPixmap('icon/about1.png'))
        self.about_me_button.setIcon(icon)
        self.about_me_button.setIconSize(self.download_button.size())





        # telegram_button
        self.telegram_button = QPushButton('', self)
        self.telegram_button.move(250, 350)
        self.telegram_button.resize(35, 35)
        self.telegram_button.setStyleSheet("background-color: #3d3d3d; color: #000000; border-radius : 5px;")
        icon = QIcon(QPixmap('icon/telegram.png'))
        self.telegram_button.setIcon(icon)
        self.telegram_button.setIconSize(self.download_button.size())



        # combo box
        self.combo1 = QComboBox(self)
        self.combo1.setGeometry(85, 200, 120, 30)
        self.combo1.setObjectName("combo1")







        self.combo1.addItem("Electro")
        self.combo1.addItem("403.Online")
        self.combo1.addItem("Radargame")
        self.combo1.addItem("Shatel")
        self.combo1.addItem("Shecan")
        self.combo1.addItem("Bogzar")
        self.combo1.addItem("Google")
        self.combo1.addItem("Open DNS")
        self.combo1.addItem("Quad9")
        self.combo1.addItem("Cloud Flare")
        self.combo1.addItem("Comodo")
        self.combo1.addItem("AdGuard")
        self.combo1.addItem("Norton")
        self.combo1.addItem("Clean")
        self.combo1.addItem("Yandex")
        self.combo1.addItem("Level 3")
        self.combo1.setStyleSheet("background-color: #000000; color: #FFFFFF; border-radius : 5px; font-size: 14px;")

        # combo_icon
        icon = QIcon("icon/Electro.png")
        self.combo1.setItemIcon(0, icon)
        icon = QIcon("icon/403.Online.png")
        self.combo1.setItemIcon(1, icon)
        icon = QIcon("icon/Radargame.png")
        self.combo1.setItemIcon(2, icon)
        icon = QIcon("icon/Shatel.png")
        self.combo1.setItemIcon(3, icon)
        icon = QIcon("icon/shecan.png")
        self.combo1.setItemIcon(4, icon)
        icon = QIcon("icon/Bogzar.png")
        self.combo1.setItemIcon(5, icon)
        icon = QIcon("icon/google.png")
        self.combo1.setItemIcon(6, icon)
        icon = QIcon("icon/Open DNS.png")
        self.combo1.setItemIcon(7, icon)
        icon = QIcon("icon/Quad9.png")
        self.combo1.setItemIcon(8, icon)
        icon = QIcon("icon/Cloud Flare.png")
        self.combo1.setItemIcon(9, icon)
        icon = QIcon("icon/comodo.png")
        self.combo1.setItemIcon(10, icon)
        icon = QIcon("icon/AdGuard.png")
        self.combo1.setItemIcon(11, icon)
        icon = QIcon("icon/norton.png")
        self.combo1.setItemIcon(12, icon)
        icon = QIcon("icon/Clean.png")
        self.combo1.setItemIcon(13, icon)
        icon = QIcon("icon/yandex.png")
        self.combo1.setItemIcon(14, icon)
        icon = QIcon("icon/Level 3.png")
        self.combo1.setItemIcon(15, icon)

        combo2 = QComboBox(self)
        combo2.setGeometry(85, 260, 120, 30)
        combo2.setObjectName("combo2")  # افزودن این خط
        combo2.currentIndexChanged.connect(self.onNetworkCardSelected)  # اتصال به تابع هنگام انتخاب کارت شبکه
        for card in active_cards:
            combo2.addItem(card)
            icon = QIcon("icon/ethernet.png")
            combo2.setItemIcon(combo2.count() - 1, icon)

        combo2.setStyleSheet("background-color: #000000; color: #FFFFFF; border-radius: 5px; font-size: 14px;")

        # در تابع on_combo1_activated
        network_card = self.findChild(QComboBox, "combo2").currentText()


        # connect
        self.set_dns_button.clicked.connect(self.applyDNS)
        self.reset_dns_button.clicked.connect(self.flushDNS)

        self.download_button.clicked.connect(self.downloadApp)
        self.support_button.clicked.connect(self.donateMe)
        self.about_me_button.clicked.connect(self.aboutme)
        self.telegram_button.clicked.connect(self.telegram)


        self.addButtonEffect(self.set_dns_button)
        self.addButtonEffect(self.reset_dns_button)
        self.addButtonEffect_2(self.download_button)
        self.addButtonEffect_2(self.support_button)
        self.addButtonEffect_2(self.about_me_button)
        self.addButtonEffect_2(self.telegram_button)

    def addButtonEffect_2(self, button):
        # تعیین استایل‌های گرافیکی با استفاده از QSS
        button.setStyleSheet(
            "QPushButton {"
            "   background-color: #3d3d3d; "
            "   color: #000000; "
            "   border-radius: 5px; "
            "   font-size: 14px; "
            "}"
            "QPushButton:hover {"
            "   background-color: #474747; "  # تغییر رنگ در هنگام هاور
            "}"
        )




        self.show()


    def addButtonEffect(self, button):
        # تعیین استایل‌های گرافیکی با استفاده از QSS
        button.setStyleSheet(
            "QPushButton {"
            "   background-color: #72C3FF; "
            "   color: #000000; "
            "   border-radius: 8px; "
            "   font-size: 15px; "
            "}"
            "QPushButton:hover {"
            "   background-color: #8ecfff; "  # تغییر رنگ در هنگام هاور
            "}"
            "QPushButton:pressed {"
            "   background-color: #66afe5; "  # تغییر رنگ در لحظه فشرده‌سازی
            "}"
        )

    # del dns
    @pyqtSlot()
    def flushDNS(self):
        try:
            if self.selected_network_card and not self.is_progress_bar_active:
                # Display the "Flushing DNS" information
                new_text_1 = '  Done'
                self.dynamic_text.setStyleSheet('background-color: #3d3d3d; color: #0FFF50')

                self.dynamic_text.setText(new_text_1)

                font = self.dynamic_text.font()
                font.setPointSize(12)
                self.dynamic_text.setFont(font)

                self.dynamic_text.setMinimumSize(100, 30)
                self.dynamic_text.setMaximumSize(100, 30)

                # Start the progress bar for flushing DNS
                self.progress_bar.show()
                self.progress_bar.setValue(0)
                self.is_progress_bar_active = True

                # Simulate the progress of the DNS flushing process
                for i in range(1, 101):
                    self.progress_bar.setValue(i)
                    QApplication.processEvents()
                    # Simulate some delay (you can replace this with the actual DNS flushing process)
                    QTimer.singleShot(10, lambda: None)

                # Flush DNS
                subprocess.call(f'netsh interface ipv4 set dnsservers "{self.selected_network_card}" source=dhcp',
                                shell=True)
                subprocess.call('ipconfig /flushdns', shell=True)

                # Finish the progress bar for flushing DNS
                self.progress_bar.hide()
                self.is_progress_bar_active = False

                # Restore the old text after flushing DNS
                QTimer.singleShot(1500, lambda: self.dynamic_text.setText("     "))

        except Exception as e:
            print(e)

    # change dns
    @pyqtSlot()
    def applyDNS(self):
        dns = {
            "Electro": "78.157.42.101*78.157.42.100",
            "403.Online": "10.202.10.202*10.202.10.102",
            "Radargame": "10.202.10.10*10.202.10.11",
            "Shatel": "85.15.1.14*85.15.1.15",
            "Shecan": "178.22.122.100*185.51.200.2",
            "Bogzar": "185.55.226.26*185.55.225.25",
            "Google": "8.8.8.8*8.8.4.4",
            "Open DNS": "208.67.222.222*208.67.220.220",
            "Quad9": "9.9.9.9*149.112.112.112",
            "Cloud Flare": "1.1.1.1*1.0.0.1",
            "Comodo": "8.26.56.26*8.20.247.20",
            "AdGuard": "94.140.14.14*94.140.15.15",
            "Norton": "199.85.126.10*199.85.126.20",
            "Clean": "185.228.168.168*185.228.169.168",
            "Yandex": "77.88.8.8*77.88.8.1",
            "Level 3": "209.244.0.3*209.244.0.4",
        }

        selected_dns = self.findChild(QComboBox, "combo1").currentText()
        dns_servers = dns[selected_dns]

        dns_servers_list = dns_servers.split('*')

        # Cut dns
        dns_server1 = dns_servers_list[0].strip()
        dns_server2 = dns_servers_list[1].strip()

        try:
            if self.selected_network_card:
                # Display the DNS information
                new_text = 'Applied'
                self.dynamic_text.setStyleSheet('background-color: #3d3d3d; color: #0FFF50')
                old_text = self.dynamic_text.text()
                self.dynamic_text.setText(new_text)

                font = self.dynamic_text.font()
                font.setPointSize(12)
                self.dynamic_text.setFont(font)

                self.dynamic_text.setMinimumSize(80, 30)
                self.dynamic_text.setMaximumSize(80, 30)

                # Start the progress bar
                self.progress_bar.show()
                self.progress_bar.setValue(0)

                # Simulate the progress of the DNS applying process
                for i in range(1, 101):
                    self.progress_bar.setValue(i)
                    QApplication.processEvents()
                    # Simulate some delay (you can replace this with the actual DNS applying process)
                    QTimer.singleShot(10, lambda: None)

                # Apply DNS
                subprocess.call(f'netsh interface ip set dns "{self.selected_network_card}" static {dns_server1}',
                                shell=True)
                subprocess.call(f'netsh interface ip add dns "{self.selected_network_card}" {dns_server2} index=2',
                                shell=True)

                # Finish the progress bar
                self.progress_bar.hide()

                # Restore the old text after applying DNS
                QTimer.singleShot(1500, lambda: self.dynamic_text.setText(old_text))
        except Exception as e:
            print(e)

    def onNetworkCardSelected(self, index):
        # تابع فراخوانی شده هنگام انتخاب کارت شبکه
        self.selected_network_card = active_cards[index]

    @pyqtSlot()
    def downloadApp(self):
        webbrowser.open('https://uploadboy.com/ur-3423437/452225/Viper_Loop')




    @pyqtSlot()
    def donateMe(self):
        webbrowser.open('https://zarinp.al/mahdibalaei')

    @pyqtSlot()
    def telegram(self):
        webbrowser.open('https://t.me/Viperloop')

    @pyqtSlot()
    def aboutme(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("about")

        dialog_label = QLabel("کلیه حقوق مادی و معنوی این اثر متعلق به پدیدآورنده می باشد\nاین برنامه کاملا رایگان "
                              "است.\n دی ان اس های موجود "
                              "در برنامه فقط صرفا جمع اوری شده است و\n سرور های موجود در برنامه هیچ ارتباطی با این "
                              "برنامه ندارند \n  شما میتوانید با یک سرچ ساده در اینترنت سایت سازنده هر دی ان اس را "
                              "پیدا کنید\nدر صورت هر گونه باگ و مشکل برنامه به ایمیل زیر پیام دهید. "
                              "Email:0mahdibalaei0@gmail.com")

        # Set text interaction flag to enable selection
        dialog_label.setTextInteractionFlags(dialog_label.textInteractionFlags() | Qt.TextSelectableByMouse)

        dialog_label.setStyleSheet("color: white;font-size: 13px;")

        # Check if a layout is already set before attempting to set a new one
        if dialog.layout() is None:
            dialog_layout = QVBoxLayout(dialog)
            dialog_layout.addWidget(dialog_label)

        dialog.exec_()


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
