from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    if len(name) > 1:
        greeting = f"Hello, {name}!"
    else:
        greeting = "Hello!"

    return greeting

import random

def get_amount() -> float:
    """
    Генерируем случайную сумму на счете.

    Сумма:
    - в диапазоне от 100 до 1000000
    - float
    - не больше 2-х знаков после запятой

    :return: случайную сумму на счете
    """

    amount = round(random.uniform(100, 1000000), 2)

    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    result = True

    if len(phone_number) != 12:
        result = False

    if phone_number[0] != '+' or phone_number[1] != '7':
        result = False

    for char in phone_number[2:]:
        if not char.isdigit():
            result = False
        
    return result


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:
    """
    Проверяет возможность осуществления перевода.
    Перевод возможен если выполняется условие:
    - текущий счет (current_amount) больше или равен сумме перевода (transfer_amount)

    :param current_amount: текущий счет
    :param transfer_amount: сумма перевода
    :return: буленовское значение - bool: True - если перевод возможен,
                                          False - если денег недостаточно
    """

    transfer_amount = float(transfer_amount)
    result = current_amount >= transfer_amount

    return result


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    """
    Модерирует текст по следующим правилам.

    Требования к тексту:
    - Первая буква заглавная, остальные буквы только в нижнем регистре
    - отсутствую лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    - слова, перечисленные в переменной uncultured_words заменяются на аналогичное количество знаков #

    :param text: исходный текст
    :param uncultured_words: список запрещенных слов
    :return: текст, соответсвующий правилам
    """
    words = text.split()
    moderated_words = []

    for word in words:
        word_stripped = word.rstrip(".,!?;:")        
        punctuation = word[len(word_stripped):]
        if word_stripped .lower() in uncultured_words:
            moderated_words.append('#' * len(word_stripped) + punctuation)
        else:
            moderated_words.append(word)
    result = ' '.join(moderated_words)
    result = result.capitalize().replace('"', '').replace("'", "")

    return result


def create_request_for_loan(user_info: str) -> str:
    """
    Генерирует заявку на кредит на основе входящей строки.
    Формат входящий строки:
    
    Иванов,Петр,Сергеевич,01.01.1991,10000
    
    Что должны вернуть на ее основе:
    
    Фамилия: Иванов
    Имя: Петр
    Отчество: Сергеевич
    Дата рождения: 01.01.1991
    Запрошенная сумма: 10000
    
    :param user_info: строка с информацией о клиенте
    :return: текст кредитной заявки
    """

    user_info_list = user_info.split(',')
    last_name = user_info_list[0]
    first_name = user_info_list[1]
    middle_name = user_info_list[2]
    birth_date = user_info_list[3]
    requested_amount = user_info_list[4]

    result = f"Фамилия: {last_name}\nИмя: {first_name}\nОтчество: {middle_name}\nДата рождения: {birth_date}\nЗапрошенная сумма: {requested_amount}"
    
    return result
