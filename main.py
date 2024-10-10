import pyautogui
import pandas as pd
import time



#abrir navegador windows

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(0.2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(1)
pyautogui.press('enter')

#fazer login site

pyautogui.press('tab')
pyautogui.sleep(0.2)
pyautogui.write('exemplo@exemplo.net')
pyautogui.press('tab')
pyautogui.write('987654321')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

#importando a tabela
tabela = pd.read_csv('produtos.csv')
print(tabela)
#cadastrar produto
for linha in tabela.index:
    pyautogui.click(x=672, y=296) # click específico para meu monitor, mudar usando auxiliar para cada tela;
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.sleep(0.2)

    pyautogui.press('tab')
    marca = tabela.loc[linha,'marca']
    pyautogui.write(str(marca))
    pyautogui.sleep(0.2)

    pyautogui.press('tab')
    tipo = tabela.loc[linha,'tipo']
    pyautogui.write(str(tipo))
    pyautogui.sleep(0.2)

    pyautogui.press('tab')
    categoria = tabela.loc[linha,'categoria']
    pyautogui.write(str(categoria))
    pyautogui.sleep(0.2)

    pyautogui.press('tab')
    preco_unitario = tabela.loc[linha,'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.sleep(0.2)

    pyautogui.press('tab')
    custo = tabela.loc[linha,'custo']
    pyautogui.write(str(custo))
    pyautogui.sleep(0.2)

    pyautogui.press('tab')
    obs = tabela.loc[linha,'obs']
    if not pd.isna(obs): # condição caso não tenha observação
         pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.sleep(0.2)

# finaliza cadastro 
    pyautogui.press('tab')    
    pyautogui.press('enter')
    pyautogui.sleep(0.2)   


# rola scroll até o início da página e repete o processo
    pyautogui.scroll(5000)
