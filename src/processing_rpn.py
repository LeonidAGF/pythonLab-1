from src.brackets_validation import brackets_validation
from src.constants import BRACKETS_ERROR, OPENING_BRACKET, CLOSING_BRACKET, SPELLING_ERROR, ALL_SYMBOLS, \
    INVALID_SYMBOLS_ERROR
from src.count_rpn import count_rpn


def processing_rpn(expression: str):

    """
        Обрабатывает поданное на вход выражение, исключая из строки с ним все лишние элементы.
        Возвращает строку с рузультатом если выражение написанно написанно без ошибок, в противном случае возвращает пустую строку.
    """

    input_str:str = expression

    for el in input_str:
        if el not in ALL_SYMBOLS:
            print(INVALID_SYMBOLS_ERROR, "\"", el, "\"")
            return ""

    while "  " in input_str:
        input_str = input_str.replace("  ", " ")

    if len(input_str)==0:
        print("\"", expression, "\"", SPELLING_ERROR)
        return ""

    if brackets_validation(input_str)==0:
        print("\"",expression,"\"",BRACKETS_ERROR)
        return ""

    input_str = input_str.replace(OPENING_BRACKET, "").replace(CLOSING_BRACKET, "")

    return count_rpn(input_str)
