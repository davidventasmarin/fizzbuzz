def fizz(num):
    flag_divisible3                 = 0
    flag_divisible5                 = 0
    flag_divisible_3_5              = 0
    
    resultado_comprobacion_numeros  = 0
    resultado_texto                 = 0
    devuelvo_texto                  = 0


    numero_temporal = list(str(num))
    
    comprobacion_numeros = comprueba_numeros(num)
    if num % 3 == 0 and num % 5 == 0:
        flag_divisible_3_5 = 1
    elif num % 3 == 0:
        flag_divisible3 = 1
    elif num % 5 == 0:
        flag_divisible5 = 1

    resultado_comprobacion_flag = comprobar_flag(flag_divisible3, flag_divisible5, flag_divisible_3_5, num)
    if num == 15:
        resultado_comprobacion_numeros = 3
    elif comprobacion_numeros == 2:
        resultado_comprobacion_numeros = 2
    elif comprobacion_numeros == 1:
        resultado_comprobacion_numeros = 1
    elif comprobacion_numeros == 3:
        resultado_comprobacion_numeros = 3
    

    if resultado_comprobacion_flag == 3:
        resultado_texto = 3
    elif resultado_comprobacion_flag == 2:
        resultado_texto = 2
    elif resultado_comprobacion_flag == 1:
        resultado_texto = 1

    if resultado_comprobacion_flag > comprobacion_numeros:
        devuelvo_texto = resultado_comprobacion_flag
    elif resultado_comprobacion_flag == 0 and comprobacion_numeros == 0:
        return num
    else:
        devuelvo_texto = comprobacion_numeros

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