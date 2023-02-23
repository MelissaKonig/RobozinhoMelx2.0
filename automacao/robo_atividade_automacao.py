import pyautogui
import time
import rpa as r
import pyautogui as p
import os

# Clickar icon Chromehttps://github.com/login
p.moveTo(x=405, y=737, duration=2)
p.click(x=405, y=737)

# Mover para a barra de pesquisa e escrever link GitHub
p.moveTo(x=364, y=45, duration=2)
p.click(x=364, y=45)
p.typewrite('https://github.com/login')
p.hotkey('enter')

# Click Sing In com meu login
p.moveTo(x=619, y=413, duration=2)
p.click(x=619, y=413)

# New Repository
p.moveTo(x=270, y=172, duration=2)
p.click(x=270, y=172)

# Repository name
p.moveTo(x=572, y=333, duration=2)
p.click(x=572, y=333)
p.typewrite('Robozinho_da_Mel')
p.click(x=305, y=667)
p.scroll(-500)

# Create Repository
p.moveTo(x=387, y=614, duration=2)
p.click(x=387, y=614)
p.sleep(2)

# <> Code
p.moveTo(x=865, y=276, duration=2)
p.click(x=865, y=276)

# Copied!
p.moveTo(x=893, y=465, duration=2)
p.click(x=893, y=465)

# Barra pesquisa Windows
p.moveTo(x=703, y=744, duration=2)
p.click(x=703, y=744)

p.moveTo(x=320, y=192, duration=2)
p.click(x=320, y=192)

os.system("start cmd")
p.sleep(2)
# p.typewrite('cd Documents/ ')
# p.hotkey('enter')
# p.sleep(1)

# p.typewrite('cd RobozinhoMelx2.0/')
# p.hotkey('enter')
# p.sleep(1)

p.typewrite('git clone https://github.com/MelissaKonig/Robozinho_da_Mel.git')
p.hotkey('enter')

p.typewrite('code .')
p.hotkey('enter')
p.sleep(7)

p.moveTo(x=149, y=72, duration=2)
p.click(x=149, y=72)
p.typewrite('booora.py')
p.hotkey('enter')