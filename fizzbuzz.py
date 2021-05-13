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

    
    if num == 15:
        resultado_comprobacion_numeros = 3
    elif comprobacion_numeros == 2:
        resultado_comprobacion_numeros = 2
    elif comprobacion_numeros == 1:
        resultado_comprobacion_numeros = 1
    elif comprobacion_numeros == 3:
        resultado_comprobacion_numeros = 3
    
    resultado_comprobacion_flag = comprobar_flag(flag_divisible3, flag_divisible5, flag_divisible_3_5, num)
    if resultado_comprobacion_flag == 3:
        resultado_texto = 3
    elif resultado_comprobacion_flag == 2:
        resultado_texto = 2
    elif resultado_comprobacion_flag == 1:
        resultado_texto = 1

    devuelvo_texto         = decidir_resultado_prevalece(resultado_comprobacion_flag, resultado_comprobacion_numeros)
    imprimo_text_divisible = imprimir_texto(devuelvo_texto)
    impr_texto_o_numero    = imprimo_text_divisible_o_numero(imprimo_text_divisible, num)
    return impr_texto_o_numero

def imprimo_text_divisible_o_numero(resultado_text_divisible, numero):
    if resultado_text_divisible:
        return resultado_text_divisible
    else:
        return numero

def decidir_resultado_prevalece(comprobacion_flag, comprobacion_numeros):
    if comprobacion_flag > comprobacion_numeros:
        devuelvo_texto = comprobacion_flag
    else:
        devuelvo_texto = comprobacion_numeros
    return devuelvo_texto


def imprimir_texto(resultado):
    if resultado == 1:
        return "Fizz"
    elif resultado == 2:
        return "Buzz"
    elif resultado == 3:
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