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
from selenium import webdriver

#Agora iremos importar a data e definir o dia
import datetime
from datetime import date
#variaveis para definir o dia de hoje
dat1= date.today()
dat2= str(dat1)
dat3= dat2[8:10]

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

        navegador = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
        navegador.get("https://sgpru.sistemas.ufsc.br/agendamento/home.xhtml")
        navegador.find_element_by_xpath('//*[@id="username"]').send_keys(self.m_user.text)
        navegador.find_element_by_xpath('//*[@id="password"]').send_keys(self.s_moodle.text)
        navegador.find_element_by_xpath('//*[@id="fm1"]/div/input').click()

# Nessa segunda parte iremos agendar nossa ida ao RU no ALMOÇO (almoço ou janta, data, horario)
        navegador.find_element_by_xpath('//*[@id="menuForm:j_idt54"]/ul/li[2]/a').click()
        navegador.find_element_by_xpath('//*[@id="agendamentoForm:refeicao"]').send_keys("ARROW_DOWN")
        navegador.find_element_by_xpath('//*[@id="agendamentoForm:refeicao"]').click()
        navegador.find_element_by_xpath('//*[@id="agendamentoForm:refeicao"]').click()
        navegador.find_element_by_xpath('// *[ @ id = "agendamentoForm:dtRefeicao"]').send_keys("ARROW_DOWN")
        navegador.find_element_by_xpath('// *[ @ id = "agendamentoForm:dtRefeicao"]').click()
        navegador.find_element_by_xpath('// *[ @ id = "agendamentoForm:dtRefeicao"]'). click()
        navegador.find_element_by_xpath('//*[@id="agendamentoForm:j_idt93"]/span[2]').click()

# Na terceira etapa iremos printar o cardapio do dia para o nosso campus e dia em questão
        navegador.get("https://ru.ufsc.br/ru/")

        # Datas dos cardapios da semana (de segunda a domingo)
        data_site1 = navegador.find_element_by_xpath(
            '//*[@id="post-65"]/div[2]/table[1]/tbody/tr[2]/td[1]/strong').text[0:2]
        data_site2 = navegador.find_element_by_xpath(
            '//*[@id="post-65"]/div[2]/table[1]/tbody/tr[3]/td[1]/strong').text[0:2]
        data_site3 = navegador.find_element_by_xpath(
            '//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[1]/strong').text[0:2]
        data_site4 = navegador.find_element_by_xpath(
            '//*[@id="post-65"]/div[2]/table[1]/tbody/tr[5]/td[1]/strong').text[0:2]
        data_site5 = navegador.find_element_by_xpath(
            '//*[@id="post-65"]/div[2]/table[1]/tbody/tr[6]/td[1]/strong').text[0:2]
        data_site6 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[7]/td[1]/b').text[0:2]
        data_site7 = navegador.find_element_by_xpath(
            '//*[@id="post-65"]/div[2]/table[1]/tbody/tr[8]/td[1]/strong').text[0:2]

        # Cardapio de cada dia da semana (de segunda a domingo)
        carne1 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[2]/td[3]').text
        prep1 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[2]/td[2]').text
        complemento1 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[2]/td[4]').text
        salada1 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[2]/td[5]').text
        sobremesa1 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[2]/td[7]').text

        carne2 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[3]/td[3]').text
        prep2 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[3]/td[2]').text
        complemento2 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[3]/td[4]').text
        salada2 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[3]/td[5]').text
        sobremesa2 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[3]/td[7]').text

        carne3 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[3]').text
        prep3 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[2]').text
        complemento3 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[4]').text
        salada3 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[5]').text
        sobremesa3 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[7]').text

        carne4 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[5]/td[3]').text
        prep4 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[5]/td[2]').text
        complemento4 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[5]/td[4]').text
        salada4 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[5]/td[5]').text
        sobremesa4 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[5]/td[7]').text

        carne5 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[6]/td[3]').text
        prep5 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[6]/td[2]').text
        complemento5 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[6]/td[4]').text
        salada5 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[6]/td[5]').text
        sobremesa5 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[6]/td[7]').text

        carne6 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[7]/td[3]').text
        prep6 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[7]/td[2]').text
        complemento6 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[7]/td[4]').text
        salada6 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[7]/td[5]').text
        sobremesa6 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[7]/td[7]').text

        carne7 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[8]/td[3]').text
        prep7 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[8]/td[2]').text
        complemento7 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[8]/td[4]').text
        salada7 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[8]/td[5]').text
        sobremesa7 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[8]/td[7]').text

        # Condições para analisar o dia atual com a info da refeição do dia "x"

        if dat3 == data_site1:
            print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne1, prep1, complemento1, salada1,
                                                                         sobremesa1))

        elif dat3 == data_site2:
            print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne2, prep2, complemento2, salada2,
                                                                         sobremesa2))

        elif dat3 == data_site3:
            print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne3, prep3, complemento3, salada3,
                                                                         sobremesa3))

        elif dat3 == data_site4:
            print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne4, prep4, complemento4, salada4,
                                                                         sobremesa4))

        elif dat3 == data_site5:
            print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne5, prep5, complemento5, salada5,
                                                                         sobremesa5))

        elif dat3 == data_site6:
            print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne6, prep6, complemento6, salada6,
                                                                         sobremesa6))

        elif dat3 == data_site7:
            print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne7, prep7, complemento7, salada7,
                                                                         sobremesa7))

        else:
            print('Vish mano, ocorreu um problema ai com as datas.')
        navegador.close()


class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()