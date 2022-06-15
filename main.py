import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import requests

class Interfaz(GridLayout):
    def __init__(self, **kwargs):
        super(Interfaz,self).__init__(**kwargs)
        self.cols=3

        self.ciudad=TextInput(hint_text='Enter city',multiline=False)
        self.add_widget(self.ciudad)

        self.submit = Button(text='Submit')
        self.submit.bind(on_press=self.consultar)
        self.add_widget(self.submit)

        self.resultado=Label(text='Esperando consulta')
        self.add_widget(self.resultado)
    
    def consultar(self,obj):
        ciudad = str(self.ciudad.text)
        url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=14361693170d23bbffec093892b8f1c7"
        nueva_url=url.format(ciudad)
        respuesta=requests.get(nueva_url)
        data = respuesta.json()
        temp =data["main"]["temp"]
        min = data["main"]["temp_min"]
        max = data["main"]["temp_max"]
        pais = data["sys"]["country"]
        self.resultado.text="Temp normal C°: "+str(temp-273.15)+"\n"+"Mínima:"+str(min-273.15)+"\n"+"Máxima:"+str(max-273.15)+"\n"+"País:"+str(pais)
        


class ClimaApp(App):
    def build(self):
        return Interfaz()



if __name__=="__main__":
    ClimaApp().run()
