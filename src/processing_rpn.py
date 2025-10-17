from src.constants import SPELLING_ERROR
from src.count_rpn import count_rpn
from src.rpn_parse import rpn_parse
import re


def processing_rpn(expression: str) -> str:
    """
            Получает на вход инфиксое выражение в виде строки и преобразует его в инфиксоное выражение в виде массива токенов
            Преобразует инфиксоное выражение в виде массива токенов в обратную польскую нотацию в виде массива токенов
            Вычисляет обратную польскую нотацию
            Возвращает строку с рузультатом если выражение написанно верно, в противном случае возвращает пустую строку.
    """

    expression = re.sub(r'~ {0,}~', r'',expression)  # заменяет выражение два подряд идущих унарных минуса пустой строкой
    expression = re.sub(r'~([0-9]+(?:\.[0-9]+)?)', r'(~\1)',expression)  # заменяте выражения вида ~n на (~n)
    expression = re.sub(r'([0-9]+(?:\.[0-9]+)?) {0,}\^ {0,}([0-9]+(?:\.[0-9]+)?)', r'(\1^\2)',expression)  # заменяет выражения вида n^q а (n^q)
    expression = re.sub(r'-', r'+~', expression) # заменяет минус на плюс с унарным минусом
    expression = re.sub(r'$', r'', expression) # удоляет из строки унарный плюс
    tokens = re.findall(r"[0-9]+(?:\.[0-9]+)?|//|[-+*/^%$~]|[()]", expression) # возвращает массив со всеми числами, скобками, операциями

    try:
        result: str = count_rpn(rpn_parse(tokens))
    except Exception:
        print(SPELLING_ERROR)
        return ""
    return result
