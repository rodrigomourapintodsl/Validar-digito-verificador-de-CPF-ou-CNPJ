import re
import numpy as np


def validar_cpf(cpf : str ) -> bool:
    "Função para validar CPF pelo algoritmo de validação do digito verificador"
    cpf = str(cpf).strip()
    if not re.match(r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$', cpf):
        return False
    # Remove caracteres não numéricos
    cpf = list(cpf.translate(str.maketrans('xX', '00', '-./')))
    cpf = np.array(cpf, dtype=np.uint8)
    # Verificando se todos os dígitos são iguais (caso raro, mas inválido)
    if np.all(cpf == cpf[0]):
        return False
    # Calculando os dígitos verificadores
    digitos1 = int(cpf[9])  == np.sum(cpf[:9]  * np.array([  1,2,3,4,5,6,7,8,9],dtype=np.uint8 )) % 11 % 10
    digitos2 = int(cpf[10]) == np.sum(cpf[:10] * np.array([0,1,2,3,4,5,6,7,8,9],dtype=np.uint8 )) % 11 % 10
    if digitos1 and digitos2:
        return True
    return False

def validar_cnpj(cnpj : str) -> bool:
    "Função para validar CNPJ pelo algoritmo de validação do digito verificador"
    cnpj=str(cnpj).strip().upper()
    if not re.match(r'^[0-9A-Z]{2}\.?[0-9A-Z]{3}\.?[0-9A-Z]{3}/?[0-9A-Z]{3}[1-9A-Z]\-?[0-9]{2}$', cnpj):
        return False
    # Remove caracteres não numéricos
    cnpj = list(cnpj.translate(str.maketrans('', '', '-./')))
    # Novo CPNJ
    cnpj = [ord(x) - 48 for x in cnpj]
    cnpj = np.array(cnpj, dtype=np.uint8)
    # Verificando se todos os dígitos são iguais (caso raro, mas inválido)
    if np.all(cnpj == cnpj[0]):
        return False
    # Calculando os dígitos verificadores
    digitos1 = int(cnpj[12]) == np.sum(cnpj[:12] * np.array([  6,7,8,9,2,3,4,5,6,7,8,9],dtype=np.uint8)) % 11 % 10
    digitos2 = int(cnpj[13]) == np.sum(cnpj[:13] * np.array([5,6,7,8,9,2,3,4,5,6,7,8,9],dtype=np.uint8)) % 11 % 10
    if digitos1 and digitos2:
        return True
    return False



if __name__ == "__main__":
    # Testando a função
    for i in range(10):
        cpf = ''.join([str(i)] * 11)
        print(f"O CPF {cpf} é válido.") if validar_cpf(cpf) else print(f"O CPF {cpf} é inválido.")
    #Validar CPF
    if validar_cpf(cpf := "123.456.789-09"):
        print(f"O CPF {cpf} é válido.")  
    else :
        print(f"O CPF {cpf} é inválido.")
    #Validar CNPJ
    for cnpj in ['12.ABC.345/01DE-35',"12ABC34501DE35",12345678900005]:
        if validar_cnpj(cnpj):
            print(f"O CNPJ {cnpj} é válido.")  
        else :
            print(f"O CNPJ {cnpj} é inválido.")

    
 
