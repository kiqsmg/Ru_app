from selenium import webdriver
import datetime
from datetime import date
#variaveis para definir o dia de hoje
dat1= date.today()
dat2= str(dat1)
dat3= dat2[8:10]

navegador = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
navegador.get("https://ru.ufsc.br/ru/")

#Datas dos cardapios da semana (de segunda a domingo)
data_site1 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[2]/td[1]/strong').text[0:2]
data_site2 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[3]/td[1]/strong').text[0:2]
data_site3 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[4]/td[1]/strong').text[0:2]
data_site4 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[5]/td[1]/strong').text[0:2]
data_site5 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[6]/td[1]/strong').text[0:2]
data_site6 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[7]/td[1]/b').text[0:2]
data_site7 = navegador.find_element_by_xpath('//*[@id="post-65"]/div[2]/table[1]/tbody/tr[8]/td[1]/strong').text[0:2]

#Cardapio de cada dia da semana (de segunda a domingo)
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

#Condições para analisar o dia atual com a info da refeição do dia "x"

if dat3 == data_site1:
    print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne1, prep1, complemento1, salada1, sobremesa1))

elif dat3 == data_site2:
    print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne2, prep2, complemento2, salada2, sobremesa2))

elif dat3 == data_site3:
    print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne3, prep3, complemento3, salada3, sobremesa3))

elif dat3 == data_site4:
    print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne4, prep4, complemento4, salada4, sobremesa4))

elif dat3 == data_site5:
    print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne5, prep5, complemento5, salada5, sobremesa5))

elif dat3 == data_site6:
    print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne6, prep6, complemento6, salada6, sobremesa6))

elif dat3 == data_site7:
    print('A refeição de hoje será:\n{}\n{}\n{}\n{}\n{}.'.format(carne7, prep7, complemento7, salada7, sobremesa7))

else:
    print('Vish mano, ocorreu um problema ai com as datas.')
navegador.close()