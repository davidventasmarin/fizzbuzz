def fizz(num):
    flag_divisible3    = 0
    flag_divisible5    = 0
    flag_divisible_3_5 = 0
    
    variable_devuelta  = 0
    variable_devuelta1  = 0

    devuelvo_texto     = 0

    numero_temporal = list(str(num))
    
    comprobacion_numeros = comprueba_numeros(num)
    print("Resultado de comprobacion numero ", comprobacion_numeros)
    if num % 3 == 0 and num % 5 == 0:
        flag_divisible_3_5 = 1
    elif num % 3 == 0:
        flag_divisible3 = 1
    elif num % 5 == 0:
        flag_divisible5 = 1

    texto = comprobar_flag(flag_divisible3, flag_divisible5, flag_divisible_3_5, num)
        
    if num == 15:
        variable_devuelta = 3
    elif comprobacion_numeros == 2:
        variable_devuelta = 2
    elif comprobacion_numeros == 1:
        variable_devuelta = 1
    elif comprobacion_numeros == 3:
        variable_devuelta = 3
    

    if texto == 3:
        variable_devuelta1 = 3
    elif texto == 2:
        variable_devuelta1 = 2
    elif texto == 1:
        variable_devuelta1 = 1

    if texto > comprobacion_numeros:
        devuelvo_texto = texto
    elif texto == 0 and comprobacion_numeros == 0:
        return num
    else:
        devuelvo_texto = comprobacion_numeros

    print("Esto vale comprobación numeros", comprobacion_numeros)
    print("\n Y esto vale text", texto)
    print("\n Esto es lo que vale variable de vuelta ", variable_devuelta)
    print("\n esto es lo que vale variable de vuelta 1", variable_devuelta1)

    if devuelvo_texto == 1:
        return "Fizz"
    elif devuelvo_texto == 2:
        return "Buzz"
    elif devuelvo_texto == 3:
        return "FizzBuzz"




def comprueba_numeros(numero):
    numero_temporal = list(str(numero))
    
    flag_contiene_3_5  = 0

    for n in numero_temporal:
        if n == '3':
            flag_contiene_3_5 += 1
        if n == '5':
            flag_contiene_3_5 += 2

    if flag_contiene_3_5 == 3:
        return 3
    elif flag_contiene_3_5 == 1:
        return 1
    elif flag_contiene_3_5 == 2:
        return 2
    else:
        return 0


def comprobar_flag(flag_divisible3, flag_divisible5, flag_divisible_3_5, num):
    if flag_divisible_3_5:
        return 3
    elif flag_divisible3:
        return 1
    elif flag_divisible5:
        return 2
    else:
        return 0