import PySimpleGUI as sg

def verifica_se_e_titular(idades, titular):
    titular = titular
    if len(idades) == 0:
        tit = sg.popup_yes_no('Já Possui plano conosco?')
        titular = tit
    return titular

def geracao_da_lista(idade, titular,lista_ben,idades):
    if idade != '' and idade.isdigit():
        idade = int(idade)
        if idade <= 100 and idade >= 0:
            idades.append(idade)
            if len(idades) == 1 and titular == 'No':
                lista_ben.append(f'Titular             {idade:02d} anos')
            else: lista_ben.append(f'Dependente    {idade:02d} anos')      
        else: sg.popup_error('Só é permitida idade até 100 anos!')
    else: sg.popup_error('Digite uma IDADE valida!') 
    return [lista_ben, idades]