# BotWhatsapp
This is a Python project for sending automated messages via WhatsApp Web using the `openpyxl` library to read data from an Excel spreadsheet and `pyautogui` to control automation.

## Requirements
To use the project, you need to install the following libraries:

```bash
pip install openpyxl 
pip install pyautogui
```
## How to use

### Spreadsheet Model and Data Format

Example:

|   Name  | DDI | DDD |   Phone   |
|---------|-----|-----|-----------|
| Person1 | 55  | 21  | xxxxxxxxx |
| Person2 | 55  | 11  | xxxxxxxxx |

1. Create a spreadsheet with .xlsx named **clients**
2. Open WhatsApp Web in your browser [here](https://web.whatsapp.com/).
3. Run the project and wait for WhatsApp Web to open.
4. The project will read data from the **'clients.xlsx'** spreadsheet.
5. An automated message will be sent to each contact in the spreadsheet.

***
***
***

# BotWhatsapp
Este é um projeto em Python para envio de mensagens automáticas via WhatsApp Web usando a biblioteca `openpyxl` para ler dados de uma planilha Excel e `pyautogui` para controlar a automação.

## Requisitos
Para usar o projeto, é necessário instalar as seguintes bibliotecas:

```bash
pip install openpyxl 
pip install pyautogui
```

## Como usar

### Modelo e formato da planilha e dados
  
Exemplo:

|   Name  | DDI | DDD |   Phone   |
|---------|-----|-----|-----------|
| Person1 | 55  | 21  | xxxxxxxxx |
| Person2 | 55  | 11  | xxxxxxxxx |

1. Crie uma planilha com .xlsx chamada **clients** 
2. Abra o WhatsApp Web no seu navegador [aqui](https://web.whatsapp.com/).
3. Execute o projeto e aguarde a abertura do WhatsApp Web.
4. O projeto lerá os dados da planilha **'clients.xlsx'** 
5. Uma mensagem automática será enviada para cada contato da planilha.
