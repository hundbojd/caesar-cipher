def fool_check_lang(n):
    k = n.lower()
    while k != 'en' and k != 'ru' and k != 'анг' and k != 'рус':
        print('Please, enter the valid language (en / ru)', '\n',
              'Пожалуйста, введите подходящий язык (анг / рус)')
        k = input()
    return k


def fool_check_cd(n):
    k = n.lower()
    while k != 'c' and k != 'd' and k != 'з' and k != 'р':
        print('Please, choose C for cipher or D for decipher', '\n',
              'Пожалуйста, введите З чтобы зашифровать и Р чтобы расшифровать')
        k = input()
    return k


def fool_check_shift(n):
    k = n
    while not k.isdigit():
        print('Please, enter the step of the shift', '\n',
              'Пожалуйста, введите шаг сдвига')
        k = input()
    return int(k)


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def cipher_eng(n):
    s1 = ''
    for i in n:
        if i.islower():
            let = eng_lower_alphabet.find(i) + shift
            if let > 25:
                s1 += eng_lower_alphabet[let - 26]
            elif let < 0:
                s1 += eng_lower_alphabet[let + 26]
            else:
                s1 += eng_lower_alphabet[let]
        elif i.isupper():
            let = eng_upper_alphabet.find(i) + shift
            if let > 25:
                s1 += eng_upper_alphabet[let - 26]
            elif let < 0:
                s1 += eng_upper_alphabet[let + 26]
            else:
                s1 += eng_upper_alphabet[let]
        elif not i.isalpha():
            s1 += i
    return s1


m = input().split()
m1 = []
for i in m:
    shift = 0
    for k in i:
        if k.isalpha():
            shift += 1
    m1.append(cipher_eng(i))

print(*m1, sep=' ')
