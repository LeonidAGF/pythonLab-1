from src.constants import SPELLING_ERROR
from src.count_rpn import count_rpn
from src.rpn_parse import rpn_parse
import re

def processing_rpn(expression: str):

    """
            Получает на вход инфиксое выражение в виде строки и преобразует его в инфиксоное выражение в виде массива токенов
            Преобразует инфиксоное выражение в виде массива токенов в обратную польскую нотацию в виде массива токенов
            Вычисляет обратную польскую нотацию
            Возвращает строку с рузультатом если выражение написанно верно, в противном случае возвращает пустую строку.
    """
    expression = expression.replace("~~", "")

    expression= re.sub(r'~(\d+(?:\.\d+)?|\([^)]+\))', r'(~\1)', expression)

    expression= re.sub(r'~(\d+(?:\.\d+)?)', r'(~\1)', expression)

    expression = expression.replace("-","+~")
    expression = expression.replace("$","")

    tokens = re.findall(r'''
               \d+(?:\.\d+)?          # Числа (целые и десятичные, только положительные)
               |//                     # Оператор целочисленного деления
               |[+*/^%$-]              # Остальные операторы (бинарные)
               |[()]                  # Скобки
               |\S+?                  # Другие символы
           ''', expression, re.VERBOSE)

    #print(tokens)
    try:
        result: str = count_rpn(rpn_parse(tokens))
    except Exception:
        print(SPELLING_ERROR)
        return ""
    return result
