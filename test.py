#Teste app do RU
#Primeiro passo: Iremos instalar a biblioteca do Kivy e dar inicio ao trabalho com a mesma

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#Agora iremos importar o selenium
from selenium import webdriver

#Importar o datetime para depois pegar a data e ver o cardapio do dia
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

    def click_me(self, instance):

        navegador = webdriver.Chrome(executable_path="C:/Python/chromedriver.exe")
        navegador.get("https://sgpru.sistemas.ufsc.br/agendamento/home.xhtml")
        navegador.find_element_by_xpath('//*[@id="username"]').send_keys(self.m_user.text)
        navegador.find_element_by_xpath('//*[@id="password"]').send_keys(self.s_moodle.text)
        navegador.find_element_by_xpath('//*[@id="fm1"]/div/input').click()

# Nessa segunda parte iremos agendar nossa ida ao RU no ALMOÇO
        navegador.find_element_by_xpath('//*[@id="menuForm:j_idt54"]/ul/li[2]/a').click()
        navegador.find_element_by_xpath('//*[@id="agendamentoForm:refeicao"]').send_keys("ARROW_DOWN")
        navegador.find_element_by_xpath('//*[@id="agendamentoForm:refeicao"]').click()
        navegador.find_element_by_xpath('//*[@id="agendamentoForm:refeicao"]').click()
        navegador.find_element_by_xpath('// *[ @ id = "agendamentoForm:dtRefeicao"]').send_keys("ARROW_DOWN")
        navegador.find_element_by_xpath('// *[ @ id = "agendamentoForm:dtRefeicao"]').click()
        navegador.find_element_by_xpath('// *[ @ id = "agendamentoForm:dtRefeicao"]'). click()
        navegador.find_element_by_xpath('//*[@id="agendamentoForm:j_idt93"]/span[2]').click()

# Na terceira etapa iremos printar o cardapio do dia para o nosso campus
        navegador.get("https://ru.ufsc.br/ru/")
        cardapio2 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[2]')
        print('A refeição de hoje será:\n{}'.format(cardapio2.text))
        navegador.close()


class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()