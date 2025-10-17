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

    expression = expression.replace("~~", "")
    expression = re.sub(r'~([0-9]+(?:\.[0-9]+)?)', r'(~\1)',expression)  # заменяте выражения вида ~n на (~n)
    expression = re.sub(r'([0-9]+(?:\.[0-9]+)?) {0,}\^ {0,}([0-9]+(?:\.[0-9]+)?)', r'(\1^\2)',expression)  # заменяет выражения вида n^q а (n^q)
    expression = expression.replace("-", "+~")
    expression = expression.replace("$", "")
    tokens = re.findall(r"[0-9]+(?:\.[0-9]+)?|//|[+*/^%$-]|[()]|\S+?", expression)

    try:
        result: str = count_rpn(rpn_parse(tokens))
    except Exception:
        print(SPELLING_ERROR)
        return ""
    return result
