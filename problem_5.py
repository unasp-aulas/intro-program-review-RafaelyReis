def main(distancia):

    if distancia <= 200:
        passagem = distancia * 0.50
        return passagem
    
    elif distancia > 200 <= 400:
        passagem = distancia * 0.45
        return passagem 
    
    elif distancia > 400:
        passagem = distancia * 0.35
        return passegem
