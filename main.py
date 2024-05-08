import pyautogui, time, pandas as pd

# comando para dar um pause entre cada comando do tipo pyautogui
pyautogui.PAUSE = 0.5

#1ª faço o código abrir o meu navegaro (no meu caso é o opera)
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

# dou um sleep para q o navegador possa abrir e o código não tente digitar nada fora do navegador
time.sleep(2)

# digito o site que quero acessar
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(2)

# clico no local onde eu quero que o código faça login
pyautogui.click(x=871, y=448)
pyautogui.write('joaozin@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456789')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)

# leio a tabela onde está localizado os produtos para cadastro
tabela = pd.read_csv('produtos.csv')

# crio um loop onde vai preencher o site com os dados existentes na tabela
for linha in tabela.index:
    pyautogui.click(x=912, y=301)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if(str(tabela.loc[linha, 'obs']) != 'nan'):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('home') # existe tbm o comando scroll