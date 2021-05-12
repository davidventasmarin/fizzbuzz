def fizz(num):
    flag_contiene3     = 0
    flag_divisible3    = 0
    flag_divisible5    = 0
    flag_divisible_3_5 = 0
    flag_contiene5 = 0

    numero_temporal = list(str(num))

    for n in numero_temporal:
        if n == '3':
            flag_contiene3 = 1
    for n in numero_temporal:
        if n == '5':
            flag_contiene5 = 1
    if num % 3 == 0 and num % 5 == 0:
        flag_divisible_3_5 = 1
    elif num % 3 == 0:
        flag_divisible3 = 1
    elif num % 5 == 0:
        flag_divisible5 = 1
    else:
        texto = comprobar_flag(flag_contiene3, flag_divisible3, flag_divisible5, flag_divisible_3_5, flag_contiene5, num)
    
    
    texto = comprobar_flag(flag_contiene3, flag_divisible3, flag_divisible5, flag_divisible_3_5, flag_contiene5, num)
    return texto



def comprobar_flag(flag_contiene3, flag_divisible3, flag_divisible5, flag_divisible_3_5, flag_contiene5, num):
    if flag_divisible_3_5:
        return "FizzBuzz"
    elif flag_divisible3 or flag_contiene3:
        return "Fizz"
    elif flag_divisible5 or flag_contiene5:
        return "Buzz"
    else:
        return num