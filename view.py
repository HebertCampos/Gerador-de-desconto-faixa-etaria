import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Simulador do Valor da Taxa de Adesão', font='26')],
]

win = sg.Window('Tabela de Simulação Taxa de Adesão', layout, resizable=True)

while True:
    eventos, valores = win.read()
    if eventos == sg.WINDOW_CLOSED:
        break
