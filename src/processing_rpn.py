from src.brackets_validation import brackets_validation
from src.constants import BRACKETS_ERROR, OPENING_BRACKET, CLOSING_BRACKET, SPELLING_ERROR
from src.count_rpn import count_rpn


def processing_rpn(expression: str):

    """
        Обрабатывает поданное на вход выражение.
        Возвращает строку с рузультатом если выражение написанно верно, в противном случае возвращает пустую строку.
    """

    input_str = expression

    while "  " in input_str:
        input_str = input_str.replace("  ", " ")

    if len(input_str)==0:
        print("\"", expression, "\"", SPELLING_ERROR)
        return ""

    if brackets_validation(input_str)==0:
        print("\"",expression,"\"",BRACKETS_ERROR)
        return ""

    input_str = input_str.replace(OPENING_BRACKET, "")
    input_str = input_str.replace(CLOSING_BRACKET, "")

    return count_rpn(input_str)
