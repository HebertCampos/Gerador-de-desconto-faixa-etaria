
def main_desconto(idades, titular, valCotas):
    if titular == 'No' and idades[0] <= 38:
        desconto = 0.2
    else: desconto = 0
    idade = idades[:]
    idade.sort(reverse = True)
    
    result = zip(idade)
    return result