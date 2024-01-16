import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui


webbrowser.open('https://web.whatsapp.com/')
sleep(20)
pyautogui.hotkey('ctrl','w')
workbook = openpyxl.load_workbook('clients.xlsx')
clients_page = workbook['Planilha1']

for line in clients_page.iter_rows(min_row=2):
    name = line[0].value
    ddi = line[1].value
    ddd = line[2].value
    phone = line[3].value
    message = f'Olá {name}, bom dia! Esta é uma mensagem automática criada por mim.'
    try:
        link_message_whatsapp = f'https://web.whatsapp.com/send?phone={ddi}{ddd}{phone}&text={quote(message)}'
        webbrowser.open(link_message_whatsapp)
        sleep(10)
        input_button = pyautogui.press('enter')
        sleep(10)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print(f'Não foi possível enviar mensagem para {name}')
        with open('errors.csv', 'a', newline='', encoding='utf-8') as archive:
            archive.write(f'{name}, {phone} ')
            pyautogui.hotkey('ctrl','w')