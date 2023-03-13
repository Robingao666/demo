# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import json
import random
from urllib import parse
import http.client
import uuid
import requests
import hashlib
import time
from imp import reload


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPixelSize(3.5+12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(20, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox_b_1 = QtWidgets.QComboBox(self.tab)
        self.comboBox_b_1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_b_1.setObjectName("comboBox_b_1")
        self.comboBox_b_1.addItem("")
        self.comboBox_b_1.addItem("")
        self.comboBox_b_1.addItem("")
        self.comboBox_b_1.addItem("")
        self.comboBox_b_1.addItem("")
        self.comboBox_b_1.addItem("")
        self.comboBox_b_1.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_b_1)
        self.pushButton_b = QtWidgets.QPushButton(self.tab)
        self.pushButton_b.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_b.setObjectName("pushButton_b")
        self.horizontalLayout_4.addWidget(self.pushButton_b)
        self.comboBox_b_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_b_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_b_2.setObjectName("comboBox_b_2")
        self.comboBox_b_2.addItem("")
        self.comboBox_b_2.addItem("")
        self.comboBox_b_2.addItem("")
        self.comboBox_b_2.addItem("")
        self.comboBox_b_2.addItem("")
        self.comboBox_b_2.addItem("")
        self.comboBox_b_2.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_b_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.textEdit_b_1 = QtWidgets.QTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(3.5+10)
        self.textEdit_b_1.setFont(font)
        self.textEdit_b_1.setObjectName("textEdit_b_1")
        self.verticalLayout_2.addWidget(self.textEdit_b_1)
        self.textEdit_b_2 = QtWidgets.QTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(3.5+10)
        self.textEdit_b_2.setFont(font)
        self.textEdit_b_2.setObjectName("textEdit_b_2")
        self.verticalLayout_2.addWidget(self.textEdit_b_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_y_1 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_y_1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_y_1.setObjectName("comboBox_y_1")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.comboBox_y_1.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_y_1)
        self.pushButton_y = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_y.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_y.setObjectName("pushButton_y")
        self.horizontalLayout_2.addWidget(self.pushButton_y)
        self.comboBox_y_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_y_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_y_2.setObjectName("comboBox_y_2")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.comboBox_y_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_y_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit_y_1 = QtWidgets.QTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(3.5+10)
        self.textEdit_y_1.setFont(font)
        self.textEdit_y_1.setObjectName("textEdit_y_1")
        self.verticalLayout.addWidget(self.textEdit_y_1)
        self.textEdit_y_2 = QtWidgets.QTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(3.5+10)
        self.textEdit_y_2.setFont(font)
        self.textEdit_y_2.setObjectName("textEdit_y_2")
        self.verticalLayout.addWidget(self.textEdit_y_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

####################################核心代码#################################################
        str111 = "QTabBar::tab{background-color:rbg(255,255,255,0);}" + \
                 "QTabBar::tab:selected{color:red;background-color:rbg(255,200,255);} "
        self.tabWidget.setStyleSheet(str111)
        self.pushButton_b.clicked.connect(self.baidu)
        self.pushButton_y.clicked.connect(self.youdao)

    def baidu(self):
        try:
            text = self.textEdit_b_1.toPlainText()
            url = "/api/trans/vip/translate"
            appid = "20200329000408029"    #请填写API
            secretKey = '2TxQYlFl9XE_Ffube23W'
            Lang = {"中文": 'zh', '英文': 'en', '日语': 'jp', '韩语': 'kor', '泰语': 'th', '越南语': 'vie', '俄语': 'ru'}
            from_b = self.comboBox_b_1.currentText()
            to_b = self.comboBox_b_2.currentText()
            fromLang = Lang[from_b]
            toLang = str(Lang[to_b])
            salt = random.randint(32768, 65536)
            sign = appid + text + str(salt) + secretKey
            md = hashlib.md5()
            md.update(sign.encode(encoding='utf-8'))
            sign = md.hexdigest()
            myurl = url + \
                    '?appid=' + appid + \
                    '&q=' + parse.quote(text) + \
                    '&from=' + fromLang + \
                    '&to=' + toLang + \
                    '&salt=' + str(salt) + \
                    '&sign=' + sign
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            response = httpClient.getresponse()
            html = response.read().decode('utf-8')
            html = json.loads(html)
            dst = html["trans_result"][0]["dst"]
            self.textEdit_b_2.setText(dst)
        except:
            QMessageBox.warning(self.pushButton, '警告', '错误', QMessageBox.Yes, QMessageBox.Yes)

    def youdao(self):
        def encrypt(signStr):
            hash_algorithm = hashlib.sha256()
            hash_algorithm.update(signStr.encode('utf-8'))
            return hash_algorithm.hexdigest()

        reload(sys)
        q = self.textEdit_y_1.toPlainText()
        if q is None:
            q_2 = None
        size = len(q)
        if size <= 20:
            q_2 = q
        else:
            q_2 = q[0:10] + str(size) + q[size - 10:size]

        YOUDAO_URL = 'https://openapi.youdao.com/api'
        APP_KEY = '7c62856eed0463b8'
        APP_SECRET = '3HYeqG5ers57Ffqb7VqP5X5Cpw39Xw9B'     #请填写
        salt = str(uuid.uuid1())
        signStr = APP_KEY + q_2 + salt + str(int(time.time())) + APP_SECRET
        sign = encrypt(signStr)
        Lang = {'自动识别': 'auto', '中文': 'zh-CHS', '俄文': 'ru', '白俄罗斯语': 'be', '英文': 'en',
                '日文': 'ja', '韩文': 'ko', '法文': 'fr', '西班牙文': 'es', '葡萄牙文': 'pt',
                '意大利文': 'it', '粤语': 'yue', '拉丁语': 'la', '世界语': 'eo', '菲律宾语': 'tl',
                '泰语': 'th', '索马里语': 'so', '尼泊尔语': '', '德文': 'de'
                }
        from_y = self.comboBox_y_1.currentText()
        to_y = self.comboBox_y_2.currentText()
        data = {}
        data['from'] = Lang[from_y]
        data['to'] = Lang[to_y]
        data['signType'] = 'v3'
        data['curtime'] = str(int(time.time()))
        data['appKey'] = APP_KEY
        data['q'] = q
        data['salt'] = salt
        data['sign'] = sign

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = requests.post(YOUDAO_URL, data=data, headers=headers)

        response = data
        # print(type(data))
        # print(data.content)

        data_2 = data.json()
        # print(data_2)
        data_3 = data_2['translation'][0]
        # print(data_3)
        self.textEdit_y_2.setText(data_3)

#############################################################################################



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "翻译精灵"))
        self.comboBox_b_1.setItemText(0, _translate("MainWindow", "中文"))
        self.comboBox_b_1.setItemText(1, _translate("MainWindow", "英文"))
        self.comboBox_b_1.setItemText(2, _translate("MainWindow", "日语"))
        self.comboBox_b_1.setItemText(3, _translate("MainWindow", "韩语"))
        self.comboBox_b_1.setItemText(4, _translate("MainWindow", "泰语"))
        self.comboBox_b_1.setItemText(5, _translate("MainWindow", "越南语"))
        self.comboBox_b_1.setItemText(6, _translate("MainWindow", "俄语"))
        self.pushButton_b.setText(_translate("MainWindow", "翻译→"))
        self.comboBox_b_2.setItemText(0, _translate("MainWindow", "英文"))
        self.comboBox_b_2.setItemText(1, _translate("MainWindow", "中文"))
        self.comboBox_b_2.setItemText(2, _translate("MainWindow", "日语"))
        self.comboBox_b_2.setItemText(3, _translate("MainWindow", "韩语"))
        self.comboBox_b_2.setItemText(4, _translate("MainWindow", "泰语"))
        self.comboBox_b_2.setItemText(5, _translate("MainWindow", "越南语"))
        self.comboBox_b_2.setItemText(6, _translate("MainWindow", "俄语"))
        self.textEdit_b_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:12pt; color:#7c7c7c;\">原文...</span></p></body></html>"))
        self.textEdit_b_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:12pt; color:#7e7e7e;\">译文...</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "百度翻译"))
        self.comboBox_y_1.setItemText(0, _translate("MainWindow", "自动识别"))
        self.comboBox_y_1.setItemText(1, _translate("MainWindow", "中文"))
        self.comboBox_y_1.setItemText(2, _translate("MainWindow", "俄文"))
        self.comboBox_y_1.setItemText(3, _translate("MainWindow", "白俄罗斯语"))
        self.comboBox_y_1.setItemText(4, _translate("MainWindow", "英文"))
        self.comboBox_y_1.setItemText(5, _translate("MainWindow", "德文"))
        self.comboBox_y_1.setItemText(6, _translate("MainWindow", "日文"))
        self.comboBox_y_1.setItemText(7, _translate("MainWindow", "韩文"))
        self.comboBox_y_1.setItemText(8, _translate("MainWindow", "法文"))
        self.comboBox_y_1.setItemText(9, _translate("MainWindow", "西班牙文"))
        self.comboBox_y_1.setItemText(10, _translate("MainWindow", "葡萄牙文"))
        self.comboBox_y_1.setItemText(11, _translate("MainWindow", "意大利文"))
        self.comboBox_y_1.setItemText(12, _translate("MainWindow", "粤语"))
        self.comboBox_y_1.setItemText(13, _translate("MainWindow", "拉丁语"))
        self.comboBox_y_1.setItemText(14, _translate("MainWindow", "世界语"))
        self.comboBox_y_1.setItemText(15, _translate("MainWindow", "菲律宾语"))
        self.comboBox_y_1.setItemText(16, _translate("MainWindow", "泰语"))
        self.comboBox_y_1.setItemText(17, _translate("MainWindow", "索马里语"))
        self.comboBox_y_1.setItemText(18, _translate("MainWindow", "尼泊尔语"))
        self.pushButton_y.setText(_translate("MainWindow", "翻译→"))
        self.comboBox_y_2.setItemText(0, _translate("MainWindow", "英文"))
        self.comboBox_y_2.setItemText(1, _translate("MainWindow", "中文"))
        self.comboBox_y_2.setItemText(2, _translate("MainWindow", "德文"))
        self.comboBox_y_2.setItemText(3, _translate("MainWindow", "俄文"))
        self.comboBox_y_2.setItemText(4, _translate("MainWindow", "白俄罗斯语"))
        self.comboBox_y_2.setItemText(5, _translate("MainWindow", "日文"))
        self.comboBox_y_2.setItemText(6, _translate("MainWindow", "韩文"))
        self.comboBox_y_2.setItemText(7, _translate("MainWindow", "法文"))
        self.comboBox_y_2.setItemText(8, _translate("MainWindow", "西班牙文"))
        self.comboBox_y_2.setItemText(9, _translate("MainWindow", "葡萄牙文"))
        self.comboBox_y_2.setItemText(10, _translate("MainWindow", "意大利文"))
        self.comboBox_y_2.setItemText(11, _translate("MainWindow", "粤语"))
        self.comboBox_y_2.setItemText(12, _translate("MainWindow", "拉丁语"))
        self.comboBox_y_2.setItemText(13, _translate("MainWindow", "世界语"))
        self.comboBox_y_2.setItemText(14, _translate("MainWindow", "菲律宾语"))
        self.comboBox_y_2.setItemText(15, _translate("MainWindow", "泰语"))
        self.comboBox_y_2.setItemText(16, _translate("MainWindow", "索马里语"))
        self.comboBox_y_2.setItemText(17, _translate("MainWindow", "尼泊尔语"))
        self.textEdit_y_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:12pt; color:#7c7c7c;\">原文...</span></p></body></html>"))
        self.textEdit_y_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:12pt; color:#7e7e7e;\">译文...</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "有道翻译"))


if __name__ == '__main__':
  app = QApplication(sys.argv)
  MainWindow = QMainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())