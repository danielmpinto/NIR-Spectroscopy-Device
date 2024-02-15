
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
from kivy_garden.graph import Graph, MeshLinePlot
from math import sin
import random
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer, MDDialogSupportingText, MDDialogContentContainer

# Crie um novo gráfico
graph = Graph(
    xlabel='last day',
    ylabel='Y',
    x_ticks_minor=5,
    x_ticks_major=25,
    y_ticks_major=1,
    y_grid_label=True,
    x_grid_label=True,
    padding=5,
    x_grid=True,
    y_grid=True,
    xmin=-0,
    xmax=7,
    ymin=0,
    ymax=200
)

# Crie um novo plot
plot = MeshLinePlot(color=[1, 0, 0, 1])

# Gere pontos para o plot
plot.points = [(x, random.randint(-10, 10)) for x in range(0, 101)]

# Adicione o plot ao gráfico
graph.add_plot(plot)


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
                text="Your actual glucose level is\nXXX mg / dL",
                bold = "True",
                halign="center",
            ),
            MDDialogButtonContainer(),
        ).open()
        self.ids.btnplay.icon = 'play'
    ## botao play end

class screen1(MDScreen):
    pass

class screen1_widget(MDWidget):
    pass
class screen3(MDScreen):
    pass


class AwesomeApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        sm = MDScreenManager()
        sm.add_widget(screen1(name='chart'))
        sm.add_widget(screen2(name='index'))
        sm.add_widget(screen3(name='user'))
        sm.current = 'index'
        
        return sm

    # muda screen


if __name__ == '__main__':
	AwesomeApp().run()
