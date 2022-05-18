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
#MICHAEL'S CODE
from jnius import autoclass
from android.runnable import run_on_ui_thread

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.kivy.android.PythonActivity').mActivity
# END OF MICHAEL'S CODE

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

    @run_on_ui_thread
    def click_me(self, instance):
        webview = WebView(activity)
        webview.getSettings().setJavaScriptEnabled(True)
        wvc = WebViewClient();
        webview.setWebViewClient(wvc);

        activity.setContentView(webview)
        webview.get('https://sgpru.sistemas.ufsc.br/agendamento/home.xhtml')
        webview.find_element_by_xpath('//*[@id="username"]').send_keys(self.m_user.text)
        webview.find_element_by_xpath('//*[@id="password"]').send_keys(self.s_moodle.text)
        webview.find_element_by_xpath('//*[@id="fm1"]/div/input').click()

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()