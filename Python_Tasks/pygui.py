import pyautogui as pag
import time




def open_vscode():
    pag.hotkey('win', 'r')  
    time.sleep(0.5)
    pag.write('code')  
    pag.press('enter')

def install_extension(extension_name):
    time.sleep(2)
    pag.hotkey('ctrl', 'p')  # Open command palette
    time.sleep(1)
    pag.write(f'ext install {extension_name}')  # Type command to install extension
    time.sleep(3)  
    
    pag.press('enter')  
    time.sleep(3) 

    # Here, locate the "Install" button and click it
    # Using a screenshot approach:
    install_button_location = pag.locateOnScreen('Embedded-Linux/Python_Tasks/screenshot.png', confidence=0.8)
    if install_button_location:
        pag.click(install_button_location)
    else:
        print(f"Couldn't find the Install button for {extension_name}")

    time.sleep(5)  # Wait for installation to complete

open_vscode()
extensions = [
    "clangd",
    "c++ testmate",
    "c++ helper",
    "cmake",
    "cmake tools"
]

for extension in extensions:
    install_extension(extension)

