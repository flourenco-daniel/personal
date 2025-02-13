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
