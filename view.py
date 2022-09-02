import PySimpleGUI as sg

sg.theme('Reddit')

idades = []
ben = len(idades)
lista_ben = []
titular = ''
parcelas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', ]

col1 = sg.Column(
    [
        [sg.Frame('Beneficiários:', [
            [sg.Text('Idade: '), sg.InputText(key='INP-idade', size=(3, 1)),
             sg.Text('          '), sg.Button('Incluir'), sg.Text('', size=(117, 2))],
            [sg.Text('Tipo            '), sg.Text('Idade')],
            [sg.Column([[sg.Listbox([x for x in lista_ben], key='-OUT-listBen', size=(60, 5)), ]]),
             sg.Column([[sg.Button('Deletar'), sg.Button('Limpar'), sg.Button('Editar Idade')]]), ],
            [sg.Text('A Taxa será dividida em:'), sg.Combo(
                parcelas, key='-parcelas-', default_value='12')],
            [sg.Button('Simular')]
        ])]
    ]
)

layout = [
    [sg.Text('Simulador do Valor da Taxa de Adesão', font='26')],
    [col1]
]

win = sg.Window('Tabela de Simulação Taxa de Adesão', layout, resizable=True)

while True:
    eventos, valores = win.read()
    if eventos == sg.WINDOW_CLOSED:
        break
