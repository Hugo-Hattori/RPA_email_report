#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui
import time
import pandas as pd
import pyperclip #copia e cola o texto para casos de uso de caracteres especiais

pyautogui.PAUSE = 1

#Passo 1: Abrir o a página de login do sistema

#Abre nova janela caso navegador esteja fechado
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(5)

pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)

#Passo 2: Preencher o login
pyautogui.click(x=968, y=376)
pyautogui.write(username)

#Passo 3: Preencher a senha
pyautogui.click(x=968, y=452)
pyautogui.write(password)

#Passo 4: Apertar em acessar
pyautogui.click(x=968, y=525)
time.sleep(5)

#Passo 5: Selecionar arquivo com dados do relatório
pyautogui.click(x=420, y=459)

#Passo 6: Baixar arquivo
pyautogui.click(x=545, y=200)


# In[2]:


#Passo 7: Cálculo dos indicadores
tabela = pd.read_csv(r"C:\Users\Hugo\Downloads\Compras.csv", sep=";")

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto/quantidade

time.sleep(5)


# In[3]:


#Passo 8: Entrar no e-mail: https://mail.google.com/mail/u/0/?tab=om#inbox
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/?tab=om#inbox")
pyautogui.press("enter")
time.sleep(5)

#Passo 9: Clicar em "escrever"
pyautogui.click(x=138, y=195)
time.sleep(5)
#Passo 10: escrever o destinatário
pyautogui.write("136493140+Hugo-Hattori@users.noreply.github.com")
pyautogui.press("tab") #confirma o destinatário
pyautogui.press("tab") #passa para o próximo campo

#Passo 11: escrever assunto
pyperclip.copy("Relatório de Compras") 
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")

#Passo 12: escrever corpo do texto
texto = f"""
Prezados,
Segue resumo das compras:

Gasto Total: R${total_gasto:,.2f}
Quantidade: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Att.,
Hugo Hatori"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")

pyautogui.hotkey("ctrl","enter") #envia o e-mail

