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
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def decipher_eng(n):
    s1 = ''
    for i in n:
        if i.islower():
            let = eng_lower_alphabet.find(i) - shift
            if let > 25:
                s1 += eng_lower_alphabet[let - 26]
            elif let < 0:
                s1 += eng_lower_alphabet[let + 26]
            else:
                s1 += eng_lower_alphabet[let]
        elif i.isupper():
            let = eng_upper_alphabet.find(i) - shift
            if let > 25:
                s1 += eng_upper_alphabet[let - 26]
            elif let < 0:
                s1 += eng_upper_alphabet[let + 26]
            else:
                s1 += eng_upper_alphabet[let]
        elif not i.isalpha():
            s1 += i
    return s1


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


def decipher_ru(n):
    s1 = ''
    for i in n:
        if i.islower():
            let = rus_lower_alphabet.find(i) - shift
            if let > 25:
                s1 += rus_lower_alphabet[let - 32]
            elif let < 0:
                s1 += rus_lower_alphabet[let + 32]
            else:
                s1 += rus_lower_alphabet[let]
        elif i.isupper():
            let = rus_upper_alphabet.find(i) - shift
            if let > 25:
                s1 += rus_upper_alphabet[let - 32]
            elif let < 0:
                s1 += rus_upper_alphabet[let + 32]
            else:
                s1 += rus_upper_alphabet[let]
        elif not i.isalpha():
            s1 += i
    return s1


def cipher_ru(n):
    s1 = ''
    for i in n:
        if i.islower():
            let = rus_lower_alphabet.find(i) + shift
            if let > 25:
                s1 += rus_lower_alphabet[let - 32]
            elif let < 0:
                s1 += rus_lower_alphabet[let + 32]
            else:
                s1 += rus_lower_alphabet[let]
        elif i.isupper():
            let = rus_upper_alphabet.find(i) + shift
            if let > 25:
                s1 += rus_upper_alphabet[let - 32]
            elif let < 0:
                s1 += rus_upper_alphabet[let + 32]
            else:
                s1 += rus_upper_alphabet[let]
        elif not i.isalpha():
            s1 += i
    return s1


print('Hello, i\'m here to cipher and decipher your sentences using the Caesar cipher', '\n',
      'Привет, я здесь, чтобы зашифровывать и расшифровывать твои предложения при помощи Шифра Цезаря')
print()
print('First of all, choose your language: en / ru', '\n',
      'Для начала выбери свой язык: анг / рус')
lang = fool_check_lang(input())

if lang == 'en' or lang == 'анг':
    print('Okay, now tell me, what is the language of your sentence?(en / ru)')
    sent_lang = fool_check_lang(input())
    print('Do you want to cipher or decipher? c / d')
    cd = fool_check_cd(input())
    print('What is the step of the shift?')
    shift = fool_check_shift(input())
    print('Got it. Now enter the sentence:')
    s = input()
else:
    print('Хорошо, теперь скажи мне язык предложения?(анг / рус)')
    sent_lang = fool_check_lang(input())
    print('Предложение надо зашифровать или расшифровать? з / р')
    cd = fool_check_cd(input())
    print('Какой будет шаг сдвига?')
    shift = fool_check_shift(input())
    print('Принято. Теперь введи предложение:')
    s = input()


if sent_lang == 'en' or sent_lang == 'анг':
    if cd == 'c' or cd == 'з':
        print(cipher_eng(s))
    else:
        print(decipher_eng(s))
else:
    if cd == 'c' or cd == 'з':
        print(cipher_ru(s))
    else:
        print(decipher_ru(s))
