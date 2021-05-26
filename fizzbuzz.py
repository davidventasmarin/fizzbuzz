def fizz(num):
    numero_temporal                = list(str(num))
    flag_divisible3                = divisible_3(num)
    flag_divisible5                = divisible_5(num)
    resultado_texto                = 0
    devuelvo_texto                 = 0
    
    
    comprobacion_numeros           = contiene_3_yo_5(numero_temporal)
    comprobacion_is_divisible      = comprobar_divisibilidad(flag_divisible3, flag_divisible5)
    resultado_comprobacion_numeros = resultado_comprobacion_flags(comprobacion_numeros)
    devuelvo_texto                 = decidir_resultado_prevalece(comprobacion_is_divisible, resultado_comprobacion_numeros)
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
    flag_numero_contenido = 0
    if '3' in numero:
        flag_numero_contenido += 1
    if '5' in numero:
        flag_numero_contenido += 2
    return flag_numero_contenido 

def comprobar_divisibilidad(is_divisible3, is_divisible5):
    devuelve_divisibilidad = 0
    if is_divisible3:
        devuelve_divisibilidad += 1
    if is_divisible5:
        devuelve_divisibilidad += 2
    return devuelve_divisibilidad

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

