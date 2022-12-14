import PySimpleGUI as sg
from controls.calculo_desconto import main_desconto

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
        
    if eventos == 'Deletar':
        try:
            id = lista_ben.index(valores['-OUT-listBen'][0])
            if titular == 'No' and id == 0:
                sg.popup_error('Não é possível apagar o titular!\n\nTente alterar a idade ou limpar a lista!')
            else:
                pop_confirm = sg.popup_ok_cancel('Certeza que deseja excluir este beneficiário?')
                if pop_confirm == 'OK': 
                    del lista_ben[id]
                    del idades[id]
                    win['-OUT-listBen'].update(lista_ben)
        except IndexError:
            sg.popup_error('Escolha um beneficiario da lista!')

    if eventos == 'Limpar':
        try:
            pop = sg.popup_ok_cancel('Certeza que deseja limpar todos beneficiários?')
            if pop == 'OK':
                lista_ben = []
                idades = []
                win['-OUT-listBen'].update(lista_ben)
                win['-parcelas-'].update('12')
                win.FindElement('_output_').Update('')
        except:
            sg.popup_error('Escolha um beneficiario!')

    if eventos == 'Editar Idade':
        try:
            id = lista_ben.index(valores['-OUT-listBen'][0])
            idadeNova=sg.popup_get_text('Modificar idade', size=(3,1))
            if idadeNova.isdigit() and idadeNova != '':
                idade = int(idadeNova)
                if idade <= 100 and idade >= 0 :
                    if id == 0:
                        lista_ben[id] = f'Titular             {idade:02d} anos'
                    else: lista_ben[id] = f'Dependente    {idade:02d} anos'
                    idades[id] = idade
                    win['-OUT-listBen'].update(lista_ben)
                else: sg.popup_error('Só é permitida idade até 100 anos!')
            else: sg.popup_error('Digite uma IDADE valida!')
        except:
            sg.popup_error('Escolha um beneficiário da lista!')

    if eventos == 'Simular':
        if len(idades) != 0:
            win.FindElement('_output_').Update('')
            divParcelas = int(valores['-parcelas-'])
            result = main_desconto(idades, titular, valCotas = 1000)
            print(result)