from selenium import webdriver
import datetime
from datetime import date


#variaveis para definir o dia de hoje
dat1= date.today()
dat2= str(dat1)
dat3= dat2[8:10]

navegador = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
navegador.get("https://ru.ufsc.br/ru/")

#variaveis para as possiveis datas de almoço
data_site1 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[2]/td[1]/strong').text[0:2]
data_site2 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[3]/td[1]/strong').text[0:2]
data_site3 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[1]/strong').text[0:2]
data_site4 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[5]/td[1]/strong').text[0:2]
data_site5 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[6]/td[1]/strong').text[0:2]
data_site6 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[7]/td[1]/strong').text[0:2]
data_site7 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[8]/td[1]/strong').text[0:2]

#variaveis de cardapios disponiveis
card_site1 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[2]/td[3]').text
card_site2 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[3]/td[3]').text
card_site3 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[3]').text
card_site4 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[5]/td[3]').text
card_site5 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[6]/td[3]').text
card_site6 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[7]/td[3]').text
card_site7 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[8]/td[3]').text

if dat3 == data_site1:
    print('A refeição de hoje será:\n {}.'.format(card_site1))
    print('A refeição de amanhã será:\n {}.'.format(card_site2))
elif dat3 == data_site2:
    print('A refeição de hoje será:\n {}.'.format(card_site2))
    print('A refeição de amanhã será:\n {}.'.format(card_site3))
elif dat3 == data_site3:
    print('A refeição de hoje será:\n {}.'.format(card_site3))
    print('A refeição de amanhã será:\n {}.'.format(card_site4))
elif dat3 == data_site4:
    print('A refeição de hoje será:\n {}.'.format(card_site4))
    print('A refeição de amanhã será:\n {}.'.format(card_site5))
elif dat3 == data_site5:
    print('A refeição de hoje será:\n {}.'.format(card_site5))
    print('A refeição de amanhã será:\n {}.'.format(card_site6))
elif dat3 == data_site6:
    print('A refeição de hoje será:\n {}.'.format(card_site6))
    print('A refeição de amanhã será:\n {}.'.format(card_site7))
elif dat3 == data_site7:
    print('A refeição de hoje será:\n {}.'.format(card_site7))
    print('A refeição de amanhã é uma surpresa')
else:
    print('Vish mano, ocorreu um problema ai com as datas.')

navegador.close()