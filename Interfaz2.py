import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.metrics import MetricsBase

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

Builder.load_file("Interfaz2.kv")

class ButtonRounded(Button):            
    def cosa(self, widget):
        # widget.background_color = (0.66, .78, .9, 1)
        # widget.background_color = (0,0,0, 1)
        # widget.canvas.color = (0.66, .78, .9, 1)
        with widget.canvas:
            Color(0.66, .78, .9)
        print("Color cambiado")
        
        
class Hola(FloatLayout):
    def pepe(self):
        pass
    
    def guardar(self, cantidad, comida):
        print(f"Guardar {cantidad.text} porciones de {comida.text}")

    def borrar(self):
        print("Borrar")
        # porciones.text = "Hola"
        
    def subir(self, widget):
        widget.text = str(int(widget.text) +1)
        
    def bajar(self,widget):
        numero = int(widget.text)
        if numero > 1:
            widget.text = str(numero-1)
            
    def actualizar_precios(self):
        print("Precios actualizados")

# class RootWidget(FloatLayout):

#     def __init__(self, **kwargs):
#         # make sure we aren't overriding any important functionality
#         super(RootWidget, self).__init__(**kwargs)

#         # boton_tirar = Button(text='Tirar',pos_hint={'x':0, 'y':0.9}, on_press=lambda x: self.cambiar_posicion(self.dados_activos))
#         # self.add_widget(boton_tirar)

#         menu_superior = RelativeLayout(pos_hint={'x':0, 'y':0.9})
#         self.add_widget(menu_superior)

#         nombre_label = Label(text="Nombre comida", pos_hint={'x':0, 'y':0.9},
#                              size_hint = (None, None),width = 50,height = 50,color="black")
#         self.add_widget(nombre_label)

#         nombre_label2 = Label(text="Nombre comida", pos=(200,500),
#                              size_hint = (None, None),width = 50,height = 50,color="black")
#         menu_superior.add_widget(nombre_label2)


#     def tamano_fuente(self, width, boton):
#         boton.font_size = width/6


class Interfaz(App):

    def build(self):
        # from kivy.core.window import Window ## Printear la posición del mouse
        # Window.bind(mouse_pos=lambda w, p: print(str(p)))
        return Hola()
    

    # def _update_rect(self, instance, value):
    #     self.rect.pos = instance.pos
    #     self.rect.size = instance.size
    #     print(f"Width: {instance.size[0]}. Height: {instance.size[1]}")

if __name__ == '__main__':
    Interfaz().run()