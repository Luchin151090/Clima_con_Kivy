from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import requests

####### APLICACION DEL CLIMA METODO GET #############
class Contenedor(Widget):
   
    def consultar(self):

        #recuperamos el dato del text_input
        ciudad = self.ids.entrada.text
        url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=14361693170d23bbffec093892b8f1c7"
        nueva_url = url.format(ciudad)
        respuesta=requests.get(nueva_url)
        data = respuesta.json()
        temp =data["main"]["temp"]
        min = data["main"]["temp_min"]
        max = data["main"]["temp_max"]
        pais = data["sys"]["country"]

        self.lbl.text="Temp normal C°: "+str(temp-273.15)+"\n"+"Mínima:"+str(min-273.15)+"\n"+"Máxima:"+str(max-273.15)+"\n"+"País:"+str(pais)
        

class MainApp(App):
    def build(self):
        return Contenedor()

MainApp().run()
