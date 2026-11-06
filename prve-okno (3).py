from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout

class SamuelApp(App):
    def build(self) -> BoxLayout:
        koren = BoxLayout(orientation="vertical")
        koren.add_widget(Label(text="0"))

        riadok1 = BoxLayout(orientation="horizontal")
        riadok1.add_widget(Button(text="1"))
        riadok1.add_widget(Button(text="2"))
        riadok1.add_widget(Button(text="3"))

        riadok2 = BoxLayout(orientation="horizontal")
        riadok2.add_widget(Button(text="4"))
        riadok2.add_widget(Button(text="5"))
        riadok2.add_widget(Button(text="6"))

        riadok3 = BoxLayout(orientation="horizontal")
        riadok3.add_widget(Button(text="7"))
        riadok3.add_widget(Button(text="8"))
        riadok3.add_widget(Button(text="9"))

        riadok4 = BoxLayout(orientation="horizontal")
        riadok4.add_widget(Button(text="+"))
        riadok4.add_widget(Button(text="0"))
        riadok4.add_widget(Button(text="*"))
        riadok4.add_widget(Button(text="/"))
        riadok4.add_widget(Button(text="="))

        koren.add_widget(riadok1)
        koren.add_widget(riadok2)
        koren.add_widget(riadok3)
        koren.add_widget(riadok4)
        return koren

SamuelApp().run()