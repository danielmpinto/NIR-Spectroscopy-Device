
from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock 
from kivymd.uix.dialog import MDDialog

from kivymd.uix.appbar import MDActionBottomAppBarButton
from kivymd.uix.tab import (
    MDTabsItem,
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsBadge,
)
from kivymd.uix.button import MDButton, MDButtonText
##ok
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
##
from kivy_garden.graph import Graph, MeshLinePlot, Plot
from math import sin
import random
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer, MDDialogSupportingText, MDDialogContentContainer




# Crie um novo gráfico
# graph = Graph(
#     xlabel='last day',
#     ylabel='mg / dL',
#     x_ticks_minor=24,
#     x_ticks_major=1,
#     y_ticks_minor=5,
#     y_ticks_major=1,
#     y_grid_label=True,
#     x_grid_label=True,
#     padding=5,
#     x_grid=True,
#     y_grid=True,
#     xmin=-0,
#     xmax=10,
#     ymin=0,
#     ymax=250
# )

# Crie um novo plot
plot = MeshLinePlot(color=[0.2, 0.6, 1, 1])


## dados
# Gere pontos para o plots
plot.points = [(x, random.randint(80, 200)) for x in range(0, 101)]

## enddados

# Adicione o plot ao gráfico
#graph.add_plot(plot)


# Designate Our .kv design file 
Builder.load_file('update_label.kv')




        
# Declare both screens
class screen2(MDScreen):
    progress = ObjectProperty(None)  # referência para o MDCircularProgressIndicator
    time_medition = 5

    ## botao play
    def on_kv_post(self, base_widget):
        self.progress = self.ids.progress  # atribui o MDCircularProgressIndicator após a inicialização

    def start_progress(self):
        self.progress.active = True  # inicia o MDCircularProgressIndicator
        self.ids.btnplay.icon = 'timer-outline'
        Clock.schedule_once(self.stop_progress, self.time_medition)  # agenda a parada do MDCircularProgressIndicator após 2 segundos
        # start counter
    
    def stop_progress(self, dt):
        self.progress.active = False  # para o MDCircularProgressIndicator
        MDDialog(
            
            MDDialogHeadlineText(
                text="Finished measurement",
                halign="center"
            ),
            MDDialogSupportingText(
                text="Your actual glucose level is\n 80 mg / dL",
                bold = "True",
                halign="center",
            ),
            MDDialogButtonContainer(),
        ).open()
        self.ids.btnplay.icon = 'play'
    ## botao play end
    

class screen1(MDScreen):
    # adicionar grafico na screen1
    def __init__(self, **kwargs):
        super(screen1, self).__init__(**kwargs)

    def on_kv_post(self, base_widget):
        # Adiciona um MDLabel ao MDBoxLayout
        box_lay = MDBoxLayout(orientation='vertical', size_hint_y=0.5, pos_hint={"top": 0.9})  # Define tamanho e extensão do layout
        #cria grafico pela primeiara vez
        graph = Graph(
            xlabel='Last day (hour)',
            ylabel='glucose (mg / dL)',
            # linhas pequenas sao horas
            x_ticks_minor=6,
            # mostrar de 6,12,18 e 24
            x_ticks_major=6,
            # cada divisao com 5
            y_ticks_minor=5,
            # mostrar de 50 em 50 mg/dl
            y_ticks_major=50,
            y_grid_label=True,
            x_grid_label=True,
            padding=5,
            x_grid=True,
            y_grid=True,
            xmin=-0,
            # 24 horas
            xmax=24,
            ymin=0,
            # 250 mg/dl
            ymax=250
        )
        graph.add_plot(plot)
        box_lay.add_widget(graph)
        self.add_widget(box_lay)

        box_button = MDBoxLayout(orientation='horizontal', size_hint_y=0.5, pos_hint={"top": 0.3})  # Define tamanho e extensão do layout
        
        # adiciona widget atualizado na pagina
        self.add_widget(box_button)

        

    def updtGraph(self):
        # atualiza grafico
        graph = Graph(
            xlabel='last day',
            ylabel='mg / dL',
            x_ticks_minor=0,
            x_ticks_major=2,
            y_ticks_minor=1,
            # com numero em cada uma
            y_ticks_major=2,
            y_grid_label=True,
            x_grid_label=True,
            padding=5,
            x_grid=True,
            y_grid=True,
            xmin=-0,
            xmax=10,
            ymin=0,
            #10 divisoes
            ymax=10
        )
        box_lay.add_widget(graph)





    


class screen3(MDScreen):
    pass


class GlucoMeasure(MDApp):
    
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        sm = MDScreenManager()
        sm.add_widget(screen1(name='chart'))
        sm.add_widget(screen2(name='index'))
        sm.add_widget(screen3(name='about'))
        sm.current = 'index'
        
        return sm

    # muda screen


if __name__ == '__main__':
	GlucoMeasure().run()
