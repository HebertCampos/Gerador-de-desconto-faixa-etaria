import PySimpleGUI as sg

from controls.inclusao_nova_idade import geracao_da_lista, verifica_se_e_titular

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

col2 = sg.Column(
    [
        [sg.Frame('Tabela Simulada', [
            [sg.Output(size=(160, 27), key='_output_', font='courier 8', )]
        ])]
    ]
)

layout = [
    [sg.Text('Simulador do Valor da Taxa de Adesão', font='26')],
    [col1],
    [col2]
]

win = sg.Window('Tabela de Simulação Taxa de Adesão', layout, resizable=True)

while True:
    eventos, valores = win.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Incluir':
        titular = verifica_se_e_titular(idades, titular)
        listas = geracao_da_lista(valores['INP-idade'], titular, lista_ben,idades)
        try:
            win['INP-idade'].Update('')
        except:
            pass
        win['-OUT-listBen'].update(listas[0])
        