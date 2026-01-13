import pyautogui
import time
import subprocess
import pandas as pd

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

subprocess.Popen(["firefox"])
time.sleep(1)

pyautogui.click(x=1207, y=405)
pyautogui.write("francielesantos@gmail.com")
pyautogui.press("tab")
pyautogui.write("24245879")
pyautogui.click(x=902, y=537)
time.sleep(3)

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:

    pyautogui.click(x=653, y= 294)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000)
