def converter(medInicial, medFinal, val):
    if medInicial == medFinal:
        return val # proporção 1:1
    
    proporcao = {
        ('pés', 'metros'): 0.3048,
        ('metros', 'pés'): 3.281,
        ('jardas', 'metros'): 0.914,
        ('metros', 'jardas'): 1.094,
        ('jardas', 'pés'): 3,
        ('pés', 'jardas'): 1 / 3
    }

    return val * proporcao[medInicial, medFinal]