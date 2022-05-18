#Teste app do RU
#Primeiro passo: Iremos instalar a biblioteca do Kivy e dar inicio ao trabalho com a mesma
#Aqui não apenas instalamos a builbioteca, como tambem já importamos o que queremos dela
#Layout--> gridlayout
#Label ---> Label
#textInput---> Textinput
#Button---> Button

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#Agora iremos importar o selenium
from appium import webdriver
from selenium.webdriver.common.by import By
capabilities = {
  'platformName': 'Android',
  'platformVersion': '9',
  'deviceName': 'Galaxy A8 (2018)',
  'automationName': 'UIAutomator2',
  'app': 'MEU RU.V13.apk',
  'browserName': 'Browser'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
driver.get('http://saucelabs.com/test/guinea-pig');
div = driver.find_element_by_id('i_am_an_id')
assertEqual('I am a div', div.text)
driver.find_element_by_id('comments').send_keys('My comment')
driver.quit()


#Aqui começaremos a criar o app propriamente dito (pelo menos o layout dele)
class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp, self).__init__()
        self.cols = 2

#Aqui iremos criar a variável do user do Moodle
        self.add_widget(Label(text = 'Moodle User:'))
        self.m_user = TextInput()
        self.add_widget(self.m_user)

#Aqui iremos criar a variável da senha do Moodle
        self.add_widget(Label(text='Senha Moodle:'))
        self.s_moodle = TextInput()
        self.add_widget(self.s_moodle)

#Agora estamos criando o botão para deixar salvo as infos anteriores
        self.press = Button(text = 'Press Here')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

#Agora iremos direcionar o app para a web usando as funções do selenium
    #Iremos utilizar as variaveis de user e senha criadas anteriormente para dar como input de text nas areas de acesso no site

    def click_me(self, instance):
        print('Hello Wold!')

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()