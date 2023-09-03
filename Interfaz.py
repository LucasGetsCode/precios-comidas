import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config


Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # boton_tirar = Button(text='Tirar',pos_hint={'x':0, 'y':0.9}, on_press=lambda x: self.cambiar_posicion(self.dados_activos))
        # self.add_widget(boton_tirar)

        menu_superior = RelativeLayout(pos_hint={'x':0, 'y':0.9})
        self.add_widget(menu_superior)

        nombre_label = Label(text="Nombre comida", pos_hint={'x':0, 'y':0.9},
                             size_hint = (None, None),width = 50,height = 50,color="black")
        self.add_widget(nombre_label)

        nombre_label2 = Label(text="Nombre comida", pos=(200,500),
                             size_hint = (None, None),width = 50,height = 50,color="black")
        menu_superior.add_widget(nombre_label2)

        # for i in range(6):
        #             dado = Button(
        #                 background_normal = self.imagenes[i],
        #                 border=(0, 0, 0, 0),
        #                 size_hint = (None, None),
        #                 width = 50,
        #                 height = 50,
        #                 pos_hint = self.posiciones[i],
        #                 # pos_hint = {'x': random.uniform(0,0.8), 'y': random.uniform(0,0.8)},
        #                 on_press = (self.bloquear))
        #             self.dados.append(dado)
        #             self.add_widget(dado)
        #             if i == 5: self.sexto_dado = dado

    def tamano_fuente(self, width, boton):
        boton.font_size = width/6


class Interfaz(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
        #     # Color(1, .1, .2, 1)  # green; colors range from 0-1 not 0-255
        #     # BorderImage(source="fondo verde degradado.png", pos=self.pos, size=self.size)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        print(f"Width: {instance.size[0]}. Height: {instance.size[1]}")

if __name__ == '__main__':
    Interfaz().run()