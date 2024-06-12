def main(cargo,salario):
   
    if cargo == "junior":
        novosalario = salario * 1.15
        return novosalario
        
    elif cargo == "pleno":
       novosalario = salario * 1.26
       return novosalario

    elif cargo == "senior":
        novosalario = salario * 1.34
        return novosalario
    
    else:
        return - 1