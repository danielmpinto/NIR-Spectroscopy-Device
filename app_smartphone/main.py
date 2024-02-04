from kivy.lang import Builder
from  kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp


## pages
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        MDButton:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        MDButton:
            text: 'Quit'

<SettingsScreen>:
    BoxLayout:
        MDButton:
            text: 'My settings button'
        MDButton:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(MDScreen):
    pass

class SettingsScreen(MDScreen):
    pass


KV = '''

MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDButton:
        style: "elevated"

        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Button"
'''

    




class Example(MDApp):
    def build(self):
        sm = MDScreenManager()
        

        # md
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"  # "Purple", "Red"

        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    Example().run()