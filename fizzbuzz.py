''' Vamos a crear una kata para entrenar habilidades de desarrollo '''

def fizz(num):
    ''' Imprimir fizz si tiene o es divisible entre 3
        Imprimir Buzz si tiene o es divisible entre 5
        Imprimir fizzbuss si se dan las dos condiciones anteriores
        Imprimir el número si no se dan ninguna de las dos condiciones '''
    numero_temporal        = list(str(num))
    flag_divisible3        = divisible_3(num)
    flag_divisible5        = divisible_5(num)
    comprobacion_numeros   = contiene_3_yo_5(numero_temporal)
    is_divisible           = comprobar_divisibilidad(flag_divisible3, flag_divisible5)
    devuelvo_texto         = decidir_resultado_prevalece(is_divisible, comprobacion_numeros)
    imprimo_text_divisible = imprimir_texto(devuelvo_texto)
    impr_texto_o_numero    = imprimir_texto_si_no_es_divisible(imprimo_text_divisible, num)
    return impr_texto_o_numero

def divisible_3(num):
    ''' Ver si es divisible entre 3 '''
    resultado    = num % 3
    is_divisible = resultado == 0
    return is_divisible

def divisible_5(num):
    ''' Ver si es divisible entre 5 '''
    resultado = num % 5
    is_divisible = resultado == 0
    return is_divisible

def contiene_3_yo_5(numero):
    ''' Verificamos en el número si contiene 3 y/o 5'''
    flag_numero_contenido = 0
    if '3' in numero:
        flag_numero_contenido += 1
    if '5' in numero:
        flag_numero_contenido += 2
    return flag_numero_contenido

def comprobar_divisibilidad(is_divisible3, is_divisible5):
    ''' Debemos de mirar por que número es divisible '''
    devuelve_divisibilidad = 0
    if is_divisible3:
        devuelve_divisibilidad += 1
    if is_divisible5:
        devuelve_divisibilidad += 2
    return devuelve_divisibilidad

def decidir_resultado_prevalece(comprobacion_is_divisible, comprobacion_numeros):
    ''' Tenemos que ver si contiene 3 y 5 ya da igual que comprobemos la divisibilidad '''
    if comprobacion_is_divisible > comprobacion_numeros:
        devuelvo_texto = comprobacion_is_divisible
    else:
        devuelvo_texto = comprobacion_numeros
    return devuelvo_texto

def imprimir_texto_si_no_es_divisible(resultado_text_divisible, numero):
    ''' Comprobar si el resultado es divisible, sino, imprimir el número '''
    if resultado_text_divisible:
        return resultado_text_divisible
    return numero

def imprimir_texto(resultado):
    ''' Aquí sabemos por las flags por que número es divisible, e imprimimos el texto '''
    lista_strings = [None, "Fizz", "Buzz", "FizzBuzz"]

    return lista_strings[resultado]
