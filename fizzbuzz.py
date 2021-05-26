def fizz(num):
    flag_divisible3    = 0
    flag_divisible5    = 0
    flag_divisible_3_5 = 0
    
    #resultado_comprobacion_numeros  = 0
    resultado_texto    = 0
    devuelvo_texto     = 0


    numero_temporal = list(str(num))
    
    comprobacion_numeros = contiene_3_yo_5(numero_temporal)
    print(comprobacion_numeros)

    if num % 3 == 0 and num % 5 == 0:
        flag_divisible_3_5 = 1
    elif num % 3 == 0:
        flag_divisible3 = 1
    elif num % 5 == 0:
        flag_divisible5 = 1

    resultado_comprobacion_flag    = comprobar_flag(flag_divisible3, flag_divisible5, flag_divisible_3_5)
    resultado_comprobacion_numeros = resultado_comprobacion_flags(comprobacion_numeros)
    devuelvo_texto                 = decidir_resultado_prevalece(resultado_comprobacion_flag, resultado_comprobacion_numeros)
    imprimo_text_divisible         = imprimir_texto(devuelvo_texto)
    impr_texto_o_numero            = imprimo_text_divisible_o_numero(imprimo_text_divisible, num)
    return impr_texto_o_numero

def divisible_3(num):
    if num % 3 == 0:
        return 1

def divisible_5(num):
    if num % 5 == 0:
        return 1

def contiene_3_yo_5(numero):
    if 3 or 5 in numero:
        que_numero_contiene = verifica_que_numeros_contiene(numero)
        return que_numero_contiene

def verifica_que_numeros_contiene(numero):
    flag_numero_contenido = 0
    if '3' in numero:
        flag_numero_contenido += 1
    if '5' in numero:
        flag_numero_contenido += 2
    return flag_numero_contenido 

def comprobar_flag(flag_divisible3, flag_divisible5, flag_divisible_3_5):
    if flag_divisible_3_5:
        return 3
    elif flag_divisible3:
        return 1
    elif flag_divisible5:
        return 2
    else:
        return 0

def resultado_comprobacion_flags(cantidad_flags):
    if cantidad_flags == 2:
        resultado_comprobacion_numeros = 2
    elif cantidad_flags == 1:
        resultado_comprobacion_numeros = 1
    elif cantidad_flags == 3:
        resultado_comprobacion_numeros = 3
    else:
        resultado_comprobacion_numeros = 0
    
    return resultado_comprobacion_numeros

def decidir_resultado_prevalece(comprobacion_flag, comprobacion_numeros):
    if comprobacion_flag > comprobacion_numeros:
        devuelvo_texto = comprobacion_flag
    else:
        devuelvo_texto = comprobacion_numeros
    return devuelvo_texto

def imprimo_text_divisible_o_numero(resultado_text_divisible, numero):
    if resultado_text_divisible:
        return resultado_text_divisible
    else:
        return numero

def imprimir_texto(resultado):
    if resultado == 1:
        return "Fizz"
    elif resultado == 2:
        return "Buzz"
    elif resultado == 3:
        return "FizzBuzz"

