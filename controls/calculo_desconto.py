def define_faixa(idade):
    if idade <= 18:
        cota = 0.52
        desconto = 0
        fe = '00 a 18'
    elif idade > 18 and idade <= 23:
        cota = 0.6
        desconto = 0
        fe = '19 a 23'
    elif idade > 23 and idade <= 28:
        cota = 0.69
        desconto = 0
        fe = '24 a 28'
    elif idade > 28 and idade <= 33:
        cota = 0.79
        desconto = 0
        fe = '29 a 33'
    elif idade > 33 and idade <= 38:
        cota = 0.91
        desconto = 0
        fe = '34 a 38'
    elif idade > 38 and idade <= 43:
        cota = 1.05
        desconto = 0.25
        fe = '39 a 43'
    elif idade > 43 and idade <= 48:
        cota = 1.36
        desconto = 0.25
        fe = '44 a 48'
    elif idade > 48 and idade <= 53:
        cota = 1.77
        desconto = 0.5
        fe = '49 a 53'
    elif idade > 53 and idade <= 58:
        cota = 2.3
        desconto = 0.5
        fe = '54 a 58'
    else:
        cota = 3.12
        desconto = 1
        fe = '59 ou mais'
    val = [cota, desconto, fe]
    return val

def valor_da_taxa_desc_idade(valCota, descCota):
    txAdesao = descCota[0] * 15
    taxa = txAdesao * valCota * descCota[1]
    return taxa

def desconto_joia_dep_menor(idades):
    desc = 0
    for i in idades:
        if i <=38:
            desc += 0.2
    return desc

def main_desconto(idades, titular, valCotas):
    if titular == 'No' and idades[0] <= 38:
        desconto = 0.2
    else: desconto = 0
    idade = idades[:]
    idade.sort(reverse = True)
    faixaEtaria = [define_faixa(i) for i in idade]
    mensalidade = [faixaEtaria[m][0] * valCotas for m in range(len(faixaEtaria))]
    valorDaTaxa = [fe[0]*15*valCotas for fe in faixaEtaria]
    valorDaTaxaDescIdade = [valor_da_taxa_desc_idade(valCotas, fe) for fe in faixaEtaria]
    descontosDependente = desconto_joia_dep_menor(idades) - desconto
    
    result = zip(idade, faixaEtaria, mensalidade, valorDaTaxa, valorDaTaxaDescIdade)
    return list(result)