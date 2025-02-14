import tkinter

def testing_tkinter():
    tkinter._test()

from flexx import flx

def testing_flexx():
    class Exemplo(flx.Widget):
        def init(self):
            flx.Button(text='Olá')
            flx.Button(text='Mundo')
    a = flx.App(Exemplo, title='Flexx demonstração')
    m = a.launch()
    flx.run()


from kivy.app import App
from kivy.uix.button import Button

def testing_kivy():
    class ExemploApp(App):
        def build(self):
            return Button(text='Hello, world!')

def testing_pyforms():
    import pyforms
    from pyforms.gui.basewidget import BaseWidget
    from pyforms.controls import ControlText
    from pyforms.controls import ControlButton

    class ExemploSimples(BaseWidget):

        def __init__(self):
            super(ExemploSimples,self).__init__('ExemploSimples')
            #Definition of the forms fields
            self._nome = ControlText('Nome', 'Default value')
            self._sobrename = ControlText('Sobrenome')
            self._nomeCompleto = ControlText('Nome completo')
            self._button = ControlButton('Pressione o Botão')

            from pyforms import start_app
            start_app(ExemploSimples)

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize

def testing_pyqt():
    class HelloWindow(QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self)

            self.setMinimumSize(QSize(280, 120))
            self.setWindowTitle("Olá, Mundo! Exemplo PyQT5")

            centralWidget = QWidget(self)
            self.setCentralWidget(centralWidget)

            gridLayout = QGridLayout(self)
            centralWidget.setLayout(gridLayout)

            title = QLabel("Olá Mundo para PyQt", self)
            title.setAlignment(QtCore.Qt.AlignCenter)
            gridLayout.addWidget(title, 0, 0)

    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )

import wx

def testing_wx():
    class Janela(wx.Frame):
        def __init__(self, parent, title):
            super(Janela, self).__init__(parent, title=title, size = (400,300))
            self.panel = ExemploPainel(self)
            self.text_ctrl = wx.TextCtrl(self.panel, pos=(5, 5))
            self.btn_test = wx.Button(self.panel, label='Pressione esse componente!', pos=(5, 55))


    class ExemploPainel(wx.Panel):
        def __init__(self, parent):
            super(ExemploPainel, self).__init__(parent)


    class ExemploApp(wx.App):
        def OnInit(self):
            self.frame = Janela(parent=None, title="Janela wxPython")
            self.frame.Show()
            return True


    app = ExemploApp()
    app.MainLoop()



def testing_pyautogui():
    import pyautogui
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(100, 150)
    pyautogui.click()
    pyautogui.click(100, 200)
    pyautogui.move(0, 10)
    pyautogui.doubleClick()

import PySimpleGUI as sg

def testing_pysimplegui():

    sg.theme('DarkAmber')

    layout = [ [sg.Text('Texto na linha 1')],
    [sg.Text('Entre com um texto na linha 2'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')] ]
    window = sg.Window('Bem-Vindo ao PySimpleGUI', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        print('Você entrou com: ', values[0])

    window.close()

